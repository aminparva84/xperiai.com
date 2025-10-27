from flask import Flask, request, jsonify, send_from_directory, render_template_string
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from datetime import datetime
import os
import json
import re
import html
import requests
import boto3

# AWS credentials should be set via environment variables or AWS credentials file
# For local development, ensure AWS credentials are configured via:
# - AWS CLI: aws configure
# - Environment variables
# - IAM role (if running on EC2)
if not os.environ.get('AWS_ACCESS_KEY_ID'):
    print("⚠️  Warning: AWS credentials not found in environment variables")
    print("   Please configure AWS credentials via AWS CLI or environment variables")

app = Flask(__name__)
CORS(app)
app.secret_key = 'xperiai-secret-key-2024'

# Contact form submissions storage
contact_submissions = []

# Load existing submissions from file
try:
    with open('contact_submissions.json', 'r', encoding='utf-8') as f:
        contact_submissions = json.load(f)
except FileNotFoundError:
    contact_submissions = []

# Lambda API configuration
LAMBDA_API_URL = None

def load_lambda_config():
    """Load Lambda API configuration"""
    global LAMBDA_API_URL
    try:
        with open('lambda_agent_config.json', 'r') as f:
            config = json.load(f)
            LAMBDA_API_URL = config['chat_endpoint']
            print(f"✅ Lambda API URL loaded: {LAMBDA_API_URL}")
            return True
    except FileNotFoundError:
        print("❌ Lambda configuration not found. Please run: python deploy_lambda_agent.py")
        return False
    except Exception as e:
        print(f"❌ Error loading Lambda config: {e}")
        return False

# Load configuration immediately
load_lambda_config()

def load_constitution_context():
    """Load Constitution context from PDFs"""
    try:
        with open('PDFConst/constitution_context.txt', 'r', encoding='utf-8') as f:
            context = f.read()
            # Truncate context to fit model limits (keep first 30000 characters)
            if len(context) > 30000:
                context = context[:30000] + "\n\n[Context truncated for model limits]"
            return context
    except FileNotFoundError:
        print("Constitution context not found. Please run: python constitution_pdf_reader.py")
        return ""
    except Exception as e:
        print(f"Error loading Constitution context: {e}")
        return ""

def get_ai_response(user_message, conversation_history=None, agent_type="general"):
    """Get AI response by invoking Lambda directly"""
    try:
        # Initialize Lambda client
        lambda_client = boto3.client('lambda', region_name='us-east-1')
        
        # Prepare request payload
        payload = {
            "message": user_message,
            "agent_type": agent_type,
            "history": conversation_history or []
        }
        
        # Call Lambda function directly
        response = lambda_client.invoke(
            FunctionName='BedrockConstitutionAgent',
            Payload=json.dumps(payload)
        )
        
        # Parse response
        result = json.loads(response['Payload'].read())
        
        if result.get('statusCode') == 200:
            body = json.loads(result['body'])
            return body.get('ai_response', 'No response received')
        else:
            print(f"Lambda error: {result}")
            return "I apologize, but I'm having trouble processing your request right now. Please try again in a moment."
        
    except Exception as e:
        print(f"Error calling Lambda function: {e}")
        return "I apologize, but I'm having trouble processing your request right now. Please try again in a moment."

# Rate limiting
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://"
)
limiter.init_app(app)

# Security headers
@app.after_request
def after_request(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:;"
    return response

# Security validation functions
def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def sanitize_input(text, max_length=1000):
    """Sanitize user input to prevent XSS and injection attacks"""
    if not text:
        return ""
    
    # Limit length
    text = text[:max_length]
    
    # Remove potentially dangerous characters
    text = re.sub(r'[<>"\']', '', text)
    
    # HTML escape
    text = html.escape(text)
    
    return text.strip()

def validate_name(name):
    """Validate name field"""
    if not name or len(name.strip()) < 2:
        return False
    return len(name.strip()) <= 100

def validate_message(message):
    """Validate message field"""
    if not message or len(message.strip()) < 10:
        return False
    return len(message.strip()) <= 2000

def is_suspicious_input(text):
    """Check for suspicious patterns that might indicate spam or attacks"""
    suspicious_patterns = [
        r'<script',
        r'javascript:',
        r'on\w+\s*=',
        r'<iframe',
        r'<object',
        r'<embed',
        r'<link',
        r'<meta',
        r'<style',
        r'expression\s*\(',
        r'url\s*\(',
        r'@import',
        r'<form',
        r'<input',
        r'<textarea',
        r'<select',
        r'<button'
    ]
    
    text_lower = text.lower()
    for pattern in suspicious_patterns:
        if re.search(pattern, text_lower):
            return True
    return False

# Routes
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/src/<path:filename>')
def src_files(filename):
    return send_from_directory('src', filename)

@app.route('/public/<path:filename>')
def public_files(filename):
    return send_from_directory('public', filename)

@app.route('/send-email', methods=['POST'])
@limiter.limit("5 per minute")  # Rate limit: 5 requests per minute
def send_email():
    """Handle contact form submission"""
    try:
        # Get form data
        data = request.get_json()
        if not data:
            return jsonify({'success': False, 'message': 'No data received'}), 400
        
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        subject = data.get('subject', '').strip()
        message = data.get('message', '').strip()
        
        # Validate required fields
        if not name or not email or not subject or not message:
            return jsonify({'success': False, 'message': 'All fields are required'}), 400
        
        # Security validation
        if not validate_name(name):
            return jsonify({'success': False, 'message': 'Invalid name format'}), 400
        
        if not validate_email(email):
            return jsonify({'success': False, 'message': 'Invalid email format'}), 400
        
        if not validate_message(message):
            return jsonify({'success': False, 'message': 'Message must be between 10 and 2000 characters'}), 400
        
        # Check for suspicious input
        if is_suspicious_input(name) or is_suspicious_input(email) or is_suspicious_input(subject) or is_suspicious_input(message):
            return jsonify({'success': False, 'message': 'Invalid input detected'}), 400
        
        # Sanitize inputs
        name = sanitize_input(name, 100)
        email = sanitize_input(email, 100)
        subject = sanitize_input(subject, 200)
        message = sanitize_input(message, 2000)
        
        # Log the submission for security monitoring
        client_ip = request.remote_addr
        user_agent = request.headers.get('User-Agent', 'Unknown')
        print(f"\n=== SECURE CONTACT FORM SUBMISSION ===")
        print(f"IP: {client_ip}")
        print(f"User-Agent: {user_agent}")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Subject: {subject}")
        print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"=====================================\n")
        
        # Store contact form submission
        submission = {
            'id': len(contact_submissions) + 1,
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'ip': client_ip,
            'user_agent': user_agent
        }
        
        # Add to in-memory storage
        contact_submissions.append(submission)
        
        # Save to file for persistence
        try:
            with open('contact_submissions.json', 'w', encoding='utf-8') as f:
                json.dump(contact_submissions, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Could not save to file: {e}")
        
        # Log to console
        print(f"\n=== CONTACT FORM SUBMISSION STORED ===")
        print(f"ID: {submission['id']}")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Subject: {subject}")
        print(f"Time: {submission['timestamp']}")
        print(f"IP: {submission['ip']}")
        print(f"=====================================\n")
        
        return jsonify({
            'success': True,
            'message': 'Thank you! Our experts will call you soon to discuss your requirements.'
        })
        
    except Exception as e:
        # Log security-related errors
        print(f"\n=== SECURITY ERROR ===")
        print(f"IP: {request.remote_addr}")
        print(f"Error: {str(e)}")
        print(f"===================\n")
        return jsonify({'success': False, 'message': 'An error occurred. Please try again.'}), 500

@app.route('/admin')
def admin_login():
    """Admin login page"""
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Xperi AI - Admin Login</title>
        <style>
            body { font-family: Arial, sans-serif; background: #f5f5f5; margin: 0; padding: 20px; }
            .container { max-width: 400px; margin: 100px auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            h1 { text-align: center; color: #333; margin-bottom: 30px; }
            input[type="password"] { width: 100%; padding: 12px; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; font-size: 16px; }
            button { width: 100%; padding: 12px; background: #667eea; color: white; border: none; border-radius: 5px; font-size: 16px; cursor: pointer; }
            button:hover { background: #5a6fd8; }
            .error { color: red; text-align: center; margin-top: 10px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Admin Login</h1>
            <form method="POST">
                <input type="password" name="password" placeholder="Enter admin password" required>
                <button type="submit">Login</button>
            </form>
            <div class="error">{{ error }}</div>
        </div>
    </body>
    </html>
    ''', error=request.args.get('error', ''))

@app.route('/admin', methods=['POST'])
def admin_authenticate():
    """Admin authentication"""
    password = request.form.get('password', '')
    
    # Admin password - CHANGE THIS TO YOUR SECURE PASSWORD
    admin_password = 'XperiAI2024!'
    
    if password == admin_password:
        return redirect('/admin/dashboard')
    else:
        return redirect('/admin?error=Invalid password')

@app.route('/admin/dashboard')
def admin_dashboard():
    """Admin dashboard to view contact form submissions"""
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Xperi AI - Admin Dashboard</title>
        <style>
            body { font-family: Arial, sans-serif; background: #f5f5f5; margin: 0; padding: 20px; }
            .container { max-width: 1200px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            h1 { color: #333; margin-bottom: 30px; }
            .submission { border: 1px solid #ddd; margin: 20px 0; padding: 20px; border-radius: 5px; background: #f9f9f9; }
            .submission h3 { margin: 0 0 10px 0; color: #667eea; }
            .submission p { margin: 5px 0; }
            .submission .message { background: white; padding: 15px; border-radius: 5px; margin: 10px 0; border-left: 4px solid #667eea; }
            .submission .meta { color: #666; font-size: 14px; }
            .logout { float: right; background: #dc3545; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; }
            .logout:hover { background: #c82333; }
            .count { background: #667eea; color: white; padding: 10px; border-radius: 5px; margin-bottom: 20px; text-align: center; }
        </style>
    </head>
    <body>
        <div class="container">
            <a href="/admin" class="logout">Logout</a>
            <h1>Contact Form Submissions</h1>
            <div class="count">Total Submissions: {{ submissions|length }}</div>
            
            {% for submission in submissions %}
            <div class="submission">
                <h3>#{{ submission.id }} - {{ submission.name }}</h3>
                <p><strong>Email:</strong> {{ submission.email }}</p>
                <p><strong>Subject:</strong> {{ submission.subject }}</p>
                <div class="message">
                    <strong>Message:</strong><br>
                    {{ submission.message }}
                </div>
                <div class="meta">
                    <strong>Time:</strong> {{ submission.timestamp }} | 
                    <strong>IP:</strong> {{ submission.ip }}
                </div>
            </div>
            {% endfor %}
            
            {% if submissions|length == 0 %}
            <div class="submission">
                <h3>No submissions yet</h3>
                <p>Contact form submissions will appear here.</p>
            </div>
            {% endif %}
        </div>
    </body>
    </html>
    ''', submissions=contact_submissions)

# Chat route
@app.route('/chat')
def chat_page():
    """Serve the Constitution chat interface"""
    with open('constitution_chat.html', 'r', encoding='utf-8') as f:
        return f.read()

@app.route('/chat/send', methods=['POST'])
@limiter.limit("10 per minute")
def send_message():
    """Handle chat messages"""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        conversation_id = data.get('conversation_id', 'default')
        agent_type = data.get('agent_type', 'general')
        
        if not user_message:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        # Get conversation history
        conversation_history = data.get('history', [])
        
        # Get AI response with agent type
        ai_response = get_ai_response(user_message, conversation_history, agent_type)
        
        # Prepare response
        response_data = {
            'user_message': user_message,
            'ai_response': ai_response,
            'timestamp': datetime.now().isoformat(),
            'conversation_id': conversation_id,
            'agent_type': agent_type
        }
        
        return jsonify(response_data)
        
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@app.route('/chat/health', methods=['GET'])
def chat_health():
    """Health check for chat service"""
    return jsonify({
        'status': 'healthy',
        'lambda_api_available': LAMBDA_API_URL is not None,
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    # Initialize Lambda API
    if load_lambda_config():
        print("✅ Lambda API initialized successfully")
    else:
        print("❌ Failed to initialize Lambda API")
    
    print("Starting Xperi AI Flask Server...")
    print("Contact form submissions will be stored securely!")
    print("Admin dashboard: http://localhost:5000/admin")
    print("Admin password: XperiAI2024!")
    print("Chat interface: http://localhost:5000/chat")
    print("Server running on http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
