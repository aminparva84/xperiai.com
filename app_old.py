from flask import Flask, request, jsonify, send_from_directory, render_template_string
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from datetime import datetime
import os
import json
import re
import html

app = Flask(__name__)
CORS(app)
app.secret_key = 'xperiai-oauth2-secret-key-2024'  # Secret key for session management

# Rate limiting for security
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://"  # Use in-memory storage explicitly
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

# OAuth2 Configuration
OAUTH2_CLIENT_ID = 'dL3oxixfqZCv_K3WJy7onZ4rzTSLcXGR355'  # Your GoDaddy Client ID
OAUTH2_CLIENT_SECRET = 'GjyXJmg6S5jahgN6FoUi1n'  # Your GoDaddy Client Secret
OAUTH2_REDIRECT_URI = 'http://localhost:5000/callback'
OAUTH2_AUTH_URL = 'https://api.godaddy.com/oauth2/authorize'
OAUTH2_TOKEN_URL = 'https://api.godaddy.com/oauth2/token'

# Store OAuth2 tokens (in production, use a database)
oauth2_tokens = {}

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
    
    # Remove excessive whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def validate_name(name):
    """Validate name field"""
    if not name or len(name) < 2 or len(name) > 100:
        return False
    # Only allow letters, spaces, hyphens, and apostrophes
    return re.match(r'^[a-zA-Z\s\-\']+$', name) is not None

def validate_message(message):
    """Validate message field"""
    if not message or len(message) < 10 or len(message) > 2000:
        return False
    return True

def is_suspicious_input(text):
    """Check for suspicious patterns that might indicate spam or attacks"""
    suspicious_patterns = [
        r'<script',
        r'javascript:',
        r'data:text/html',
        r'vbscript:',
        r'onload=',
        r'onerror=',
        r'<iframe',
        r'<object',
        r'<embed',
        r'<link',
        r'<meta',
        r'bitcoin',
        r'cryptocurrency',
        r'viagra',
        r'casino',
        r'gambling',
        r'loan',
        r'credit',
        r'debt',
        r'free money',
        r'click here',
        r'buy now',
        r'act now',
        r'limited time',
        r'urgent',
        r'congratulations',
        r'winner',
        r'prize'
    ]
    
    text_lower = text.lower()
    for pattern in suspicious_patterns:
        if re.search(pattern, text_lower):
            return True
    return False

def send_email_oauth2(to_email, subject, html_content, reply_to=None):
    """Send email using SMTP authentication"""
    
    try:
        # Create message
        msg = MIMEMultipart('alternative')
        msg['From'] = 'admin@xperiai.com'
        msg['To'] = to_email
        msg['Subject'] = subject
        
        if reply_to:
            msg['Reply-To'] = reply_to
        
        # Attach HTML content
        html_part = MIMEText(html_content, 'html')
        msg.attach(html_part)
        
        # Store contact form submission in database/file
        submission = {
            'id': len(contact_submissions) + 1,
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'ip': request.remote_addr,
            'user_agent': request.headers.get('User-Agent', 'Unknown')
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
        
        return True, "Message received and stored securely!"
        
    except Exception as e:
        print(f"\n=== EMAIL ERROR ===")
        print(f"Error: {str(e)}")
        print(f"===================\n")
        return False, f"SMTP email error: {str(e)}"

@app.route('/auth')
def oauth2_auth():
    """Start OAuth2 authentication flow"""
    params = {
        'client_id': OAUTH2_CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': OAUTH2_REDIRECT_URI,
        'scope': 'email',
        'state': 'xperiai_oauth2'
    }
    
    auth_url = f"{OAUTH2_AUTH_URL}?{urlencode(params)}"
    return redirect(auth_url)

@app.route('/callback')
def oauth2_callback():
    """Handle OAuth2 callback"""
    code = request.args.get('code')
    state = request.args.get('state')
    
    if not code:
        return jsonify({'error': 'No authorization code received'}), 400
    
    # Exchange code for token
    data = {
        'grant_type': 'authorization_code',
        'client_id': OAUTH2_CLIENT_ID,
        'client_secret': OAUTH2_CLIENT_SECRET,
        'code': code,
        'redirect_uri': OAUTH2_REDIRECT_URI
    }
    
    try:
        response = requests.post(OAUTH2_TOKEN_URL, data=data)
        response.raise_for_status()
        
        token_data = response.json()
        oauth2_tokens['access_token'] = token_data.get('access_token')
        oauth2_tokens['refresh_token'] = token_data.get('refresh_token')
        
        return jsonify({
            'success': True,
            'message': 'OAuth2 authentication successful! You can now send emails.'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'OAuth2 authentication failed: {str(e)}'
        }), 500

@app.route('/send-email', methods=['POST'])
@limiter.limit("5 per minute")  # Rate limit: 5 emails per minute per IP
def send_email():
    """Handle contact form submission with comprehensive security validation"""
    try:
        # Check if request has JSON data
        if not request.is_json:
            return jsonify({
                'success': False,
                'message': 'Invalid request format. Please use JSON.'
            }), 400
        
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'email', 'subject', 'message']
        for field in required_fields:
            if not data.get(field):
                return jsonify({
                    'success': False,
                    'message': f'Missing required field: {field}'
                }), 400
        
        # Extract and validate each field
        name = data['name'].strip()
        email = data['email'].strip()
        subject = data['subject'].strip()
        message = data['message'].strip()
        
        # Security validation
        if not validate_name(name):
            return jsonify({
                'success': False,
                'message': 'Invalid name format. Please use only letters, spaces, hyphens, and apostrophes.'
            }), 400
        
        if not validate_email(email):
            return jsonify({
                'success': False,
                'message': 'Invalid email format. Please provide a valid email address.'
            }), 400
        
        if not validate_message(message):
            return jsonify({
                'success': False,
                'message': 'Message must be between 10 and 2000 characters.'
            }), 400
        
        # Check for suspicious content
        all_text = f"{name} {email} {subject} {message}"
        if is_suspicious_input(all_text):
            return jsonify({
                'success': False,
                'message': 'Your message contains suspicious content and cannot be sent.'
            }), 400
        
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
        
        # Create notification email HTML
        notification_html = f"""
        <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
            <h2 style="color: #333; border-bottom: 2px solid #667eea; padding-bottom: 10px;">
                New Contact Form Submission (OAuth2)
            </h2>
            
            <div style="background: #f8f9fa; padding: 20px; border-radius: 8px; margin: 20px 0;">
                <h3 style="color: #2d3748; margin-top: 0;">Contact Details</h3>
                <p><strong>Name:</strong> {name}</p>
                <p><strong>Email:</strong> {email}</p>
                <p><strong>Subject:</strong> {subject}</p>
                <p><strong>Date:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            </div>
            
            <div style="background: #fff; padding: 20px; border: 1px solid #e2e8f0; border-radius: 8px;">
                <h3 style="color: #2d3748; margin-top: 0;">Message</h3>
                <p style="line-height: 1.6; color: #4a5568;">{message.replace(chr(10), '<br>')}</p>
            </div>
            
            <div style="margin-top: 20px; padding: 15px; background: #e6fffa; border-left: 4px solid #10b981; border-radius: 4px;">
                <p style="margin: 0; color: #065f46; font-size: 14px;">
                    <strong>Xperi AI</strong> - OAuth2 Email Authentication
                </p>
            </div>
        </div>
        """
        
        # Create confirmation email for the user
        confirmation_html = f"""
        <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
            <h2 style="color: #333; border-bottom: 2px solid #667eea; padding-bottom: 10px;">
                Thank You for Contacting Xperi AI!
            </h2>
            
            <div style="background: #f8f9fa; padding: 20px; border-radius: 8px; margin: 20px 0;">
                <p>Hello <strong>{name}</strong>,</p>
                <p>Thank you for reaching out to us! We have received your message and will get back to you as soon as possible.</p>
                
                <div style="background: white; padding: 15px; border-left: 4px solid #667eea; margin: 15px 0;">
                    <p><strong>Your Message:</strong></p>
                    <p style="color: #666; font-style: italic;">"{message}"</p>
                </div>
                
                <p>We typically respond within 24 hours during business days.</p>
            </div>
            
            <div style="text-align: center; margin-top: 30px; padding: 20px; background: #667eea; color: white; border-radius: 8px;">
                <h3 style="margin: 0 0 10px 0;">Xperi AI Team</h3>
                <p style="margin: 0; opacity: 0.9;">
                    <strong>Xperi AI</strong> - Your AI Solutions Partner
                </p>
            </div>
        </div>
        """
        
        # Send notification email to admin
        success1, msg1 = send_email_oauth2(
            to_email='admin@xperiai.com',
            subject=f"New Contact Form Submission: {subject}",
            html_content=notification_html,
            reply_to=email
        )
        
        # Send confirmation email to user
        success2, msg2 = send_email_oauth2(
            to_email=email,
            subject=f"Thank you for contacting Xperi AI - {subject}",
            html_content=confirmation_html,
            reply_to='admin@xperiai.com'
        )
        
        if success1 and success2:
            return jsonify({
                'success': True,
                'message': 'Thank you! Your message has been received and a confirmation email has been sent to you.'
            })
        elif success1:
            return jsonify({
                'success': True,
                'message': 'Thank you! Your message has been received. (Confirmation email failed to send)'
            })
        else:
            return jsonify({
                'success': False,
                'message': f'Error: {msg1}'
            }), 500
            
    except Exception as e:
        # Log security-related errors
        print(f"\n=== SECURITY ERROR ===")
        print(f"IP: {request.remote_addr}")
        print(f"Error: {str(e)}")
        print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"=====================\n")
        
        return jsonify({
            'success': False,
            'message': 'An error occurred while processing your request. Please try again later.'
        }), 500

# Handle rate limiting errors
@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify({
        'success': False,
        'message': 'Too many requests. Please wait a moment before trying again.'
    }), 429

@app.route('/')
def serve_index():
    """Serve the main HTML file"""
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    """Serve static files"""
    return send_from_directory('.', filename)

@app.route('/status')
def oauth2_status():
    """Check OAuth2 authentication status"""
    if 'access_token' in oauth2_tokens:
        return jsonify({
            'authenticated': True,
            'message': 'OAuth2 is ready for sending emails'
        })
    else:
        return jsonify({
            'authenticated': False,
            'message': 'OAuth2 not authenticated. Visit /auth to authenticate.',
            'auth_url': '/auth'
        })

if __name__ == '__main__':
    print("Starting Xperi AI Flask Server with OAuth2...")
    print("OAuth2 Email service is ready!")
    print("Server running on http://localhost:5000")
    print()
    print("To authenticate OAuth2:")
    print("1. Get OAuth2 credentials from GoDaddy Developer Portal")
    print("2. Update OAUTH2_CLIENT_ID and OAUTH2_CLIENT_SECRET in this file")
    print("3. Visit http://localhost:5000/auth to authenticate")
    print()
    app.run(debug=True, host='0.0.0.0', port=5000)
