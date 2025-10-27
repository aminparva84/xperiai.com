#!/usr/bin/env python3
"""
Lambda that queries Bedrock Knowledge Base directly
"""

import json
import boto3
from typing import Dict, Any

def query_knowledge_base(question: str, session_id=None):
    """Query the Bedrock Agent directly"""
    bedrock_agent_runtime = boto3.client('bedrock-agent-runtime', region_name='us-east-1')
    
    try:
        # Use provided session ID or generate one
        import uuid
        if not session_id:
            session_id = f"session-{uuid.uuid4().hex[:8]}"
        
        print(f"🔍 Querying Agent: {question} (Session: {session_id})")
        
        # Invoke agent directly
        response = bedrock_agent_runtime.invoke_agent(
            agentId='TBQJ1GDUEI',
            agentAliasId='TSTALIASID',
            sessionId=session_id,
            inputText=question
        )
        
        # Read the response stream
        answer_parts = []
        for event in response['completion']:
            if 'chunk' in event:
                chunk_text = event['chunk']['bytes'].decode('utf-8')
                answer_parts.append(chunk_text)
        
        answer = ''.join(answer_parts)
        print(f"✅ Agent Response: {answer[:100]}...")
        return answer if answer else "No response generated"
    
    except Exception as e:
        print(f"❌ Error: {e}")
        return f"I apologize, but I encountered an error: {str(e)}"

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """Lambda handler"""
    try:
        if 'body' in event:
            body = json.loads(event['body']) if isinstance(event['body'], str) else event['body']
        else:
            body = event
        
        user_message = body.get('message', '').strip()
        
        if not user_message:
            return {
                'statusCode': 400,
                'headers': {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'},
                'body': json.dumps({'error': 'Message cannot be empty'})
            }
        
        # Query Knowledge Base with session ID from payload
        session_id = body.get('session_id', None)
        print(f"🔍 Querying KB for: {user_message}")
        ai_response = query_knowledge_base(user_message, session_id)
        
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({
                'user_message': user_message,
                'ai_response': ai_response
            })
        }
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': str(e)})
        }

