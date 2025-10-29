#!/usr/bin/env python3
"""
Simplified AWS Lambda function for Bedrock Constitution Agent
"""

import json
import boto3
from typing import Dict, Any

# Initialize Bedrock client
bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-east-1')

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Lambda handler for Constitution Agent API
    """
    try:
        # Parse the request
        if 'body' in event:
            # API Gateway event
            body = json.loads(event['body']) if isinstance(event['body'], str) else event['body']
        else:
            # Direct invocation
            body = event
        
        # Extract parameters
        user_message = body.get('message', '').strip()
        agent_type = body.get('agent_type', 'constitution')
        conversation_history = body.get('history', [])
        
        if not user_message:
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'POST, OPTIONS'
                },
                'body': json.dumps({'error': 'Message cannot be empty'})
            }
        
        # Get AI response
        ai_response = get_bedrock_response(user_message, agent_type)
        
        # Return response
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'POST, OPTIONS'
            },
            'body': json.dumps({
                'user_message': user_message,
                'ai_response': ai_response,
                'agent_type': agent_type,
                'timestamp': context.aws_request_id
            })
        }
        
    except Exception as e:
        print(f"Error in Lambda handler: {e}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': f'Internal server error: {str(e)}'})
        }

def apply_response_template(response_text: str, agent_type: str) -> str:
    """Apply special template to agent responses"""
    from datetime import datetime
    
    # Get current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Define agent-specific branding
    if agent_type == 'constitution':
        agent_name = "🏛️ Constitutional Law Expert"
        agent_description = "Specialized in US Constitution, Amendments, and Constitutional Law"
        template_color = "#2E8B57"  # Sea Green
    else:
        agent_name = "🤖 Xperi AI Assistant"
        agent_description = "Your AI and ML development partner"
        template_color = "#667eea"  # Blue
    
    # Create the templated response
    template = f"""
<div style="border: 2px solid {template_color}; border-radius: 12px; padding: 20px; margin: 15px 0; background: linear-gradient(135deg, #f8f9ff 0%, #ffffff 100%); box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
    <div style="display: flex; align-items: center; margin-bottom: 15px; padding-bottom: 10px; border-bottom: 2px solid {template_color};">
        <div style="font-size: 24px; margin-right: 12px;">{agent_name.split(' ')[0]}</div>
        <div>
            <h3 style="margin: 0; color: {template_color}; font-family: 'Segoe UI', Arial, sans-serif;">{agent_name.split(' ', 1)[1] if ' ' in agent_name else agent_name}</h3>
            <p style="margin: 2px 0 0 0; font-size: 12px; color: #666; font-style: italic;">{agent_description}</p>
        </div>
    </div>
    
    <div style="background: white; padding: 15px; border-radius: 8px; border-left: 4px solid {template_color}; line-height: 1.6; font-family: 'Segoe UI', Arial, sans-serif;">
        {response_text}
    </div>
    
    <div style="margin-top: 15px; padding-top: 10px; border-top: 1px solid #eee; display: flex; justify-content: space-between; align-items: center;">
        <div style="font-size: 11px; color: #888;">
            <span style="background: {template_color}; color: white; padding: 2px 6px; border-radius: 3px; margin-right: 8px;">AI Response</span>
            Generated: {timestamp}
        </div>
        <div style="font-size: 11px; color: #888;">
            Powered by <strong>Xperi AI</strong> • AWS Bedrock
        </div>
    </div>
</div>
"""
    
    return template

def get_bedrock_response(user_message: str, agent_type: str = 'constitution') -> str:
    """Get response from Bedrock"""
    try:
        if agent_type == 'constitution':
            system_prompt = """You are a specialized Legal Expert AI Assistant with deep knowledge of US Constitution, Constitutional Law, and California Criminal Law.

IMPORTANT GUIDELINES:
- ONLY answer questions about US Constitution, Constitutional Law, and California Criminal Law
- If asked about topics NOT related to these legal documents, politely respond: 'I'm sorry, but I can only answer questions about US Constitution, Constitutional Law, and California Criminal Law. I don't have information about other topics. Please ask me about constitutional provisions, amendments, legal principles, or California criminal law procedures.'
- Always cite specific constitutional provisions, statutes, or legal references when answering
- If you're unsure about a legal question, say so rather than guessing
- Focus on educational and accurate legal analysis only

Your expertise includes:
- US Constitution (all Articles and Sections)
- Bill of Rights (Amendments 1-10)
- Constitutional Amendments (11-27)
- Constitutional Law principles and doctrines
- California Criminal Law and procedures
- Federal and state legal frameworks
- Historical context and interpretation
- Supreme Court decisions and precedents
- Federalism and separation of powers
- Due process and equal protection
- Constitutional rights and liberties
- Criminal law procedures and rights

Always be precise, educational, and cite specific legal provisions when relevant. If you're unsure about something, say so rather than guessing."""
        else:
            system_prompt = """You are Xperi AI Assistant, a helpful AI assistant for Xperi AI, a leading AI and ML development company in California. 
            
            You help with:
            - AI and ML development questions
            - Software development inquiries
            - Technical consulting
            - Project planning and strategy
            - Resume and career advice
            - General technology questions
            
            Be professional, helpful, and knowledgeable. Keep responses concise but informative."""
        
        # Prepare the request
        request_body = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 2000 if agent_type == "constitution" else 1000,
            "messages": [
                {
                    "role": "user",
                    "content": f"{system_prompt}\n\nHuman: {user_message}\n\nAssistant:"
                }
            ]
        }
        
        # Call Bedrock with Titan (optimized for speed)
        titan_request = {
            "inputText": f"{system_prompt}\n\nHuman: {user_message}\n\nAssistant:",
            "textGenerationConfig": {
                "maxTokenCount": 500,  # Reduced for faster response
                "temperature": 0.7,
                "topP": 0.9
            }
        }
        
        response = bedrock_runtime.invoke_model(
            modelId="amazon.titan-text-express-v1",
            body=json.dumps(titan_request),
            contentType="application/json"
        )
        
        # Parse response
        response_body = json.loads(response['body'].read())
        raw_response = response_body['results'][0]['outputText']
        
        # Apply template to the response
        templated_response = apply_response_template(raw_response, agent_type)
        
        return templated_response
        
    except Exception as e:
        print(f"Error in Bedrock call: {e}")
        error_message = "I apologize, but I'm having trouble processing your request right now. Please try again in a moment."
        return apply_response_template(error_message, agent_type)
