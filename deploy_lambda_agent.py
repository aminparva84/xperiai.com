#!/usr/bin/env python3
"""
Deploy Lambda function for Bedrock Constitution Agent
"""

import boto3
import json
import zipfile
import os
import time

def create_lambda_package():
    """Create deployment package for Lambda"""
    print("📦 Creating Lambda deployment package...")
    
    # Create deployment directory
    os.makedirs('lambda_deployment', exist_ok=True)
    
    # Copy the Lambda function
    with open('lambda_with_kb.py', 'r', encoding='utf-8') as f:
        lambda_code = f.read()
    
    with open('lambda_deployment/lambda_function.py', 'w', encoding='utf-8') as f:
        f.write(lambda_code)
    
    # Create requirements.txt for Lambda (minimal - just boto3)
    with open('lambda_deployment/requirements.txt', 'w') as f:
        f.write("boto3==1.34.0\n")
    
    # Install dependencies
    print("📥 Installing dependencies...")
    os.system("cd lambda_deployment && pip install -r requirements.txt -t .")
    
    # Create zip file
    print("🗜️ Creating deployment package...")
    with zipfile.ZipFile('lambda_deployment.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk('lambda_deployment'):
            for file in files:
                file_path = os.path.join(root, file)
                arc_path = os.path.relpath(file_path, 'lambda_deployment')
                zipf.write(file_path, arc_path)
    
    print("✅ Lambda package created: lambda_deployment.zip")
    return 'lambda_deployment.zip'

def create_lambda_function():
    """Create Lambda function"""
    print("🚀 Creating Lambda function...")
    
    # Create deployment package
    package_path = create_lambda_package()
    
    # Initialize AWS clients
    lambda_client = boto3.client('lambda', region_name='us-east-1')
    iam_client = boto3.client('iam', region_name='us-east-1')
    
    # Create IAM role for Lambda
    role_name = 'BedrockAgentLambdaRole'
    try:
        # Try to get existing role
        role_response = iam_client.get_role(RoleName=role_name)
        role_arn = role_response['Role']['Arn']
        print(f"✅ Using existing role: {role_arn}")
    except iam_client.exceptions.NoSuchEntityException:
        # Create new role
        print("🔧 Creating IAM role for Lambda...")
        
        trust_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "lambda.amazonaws.com"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        }
        
        role_response = iam_client.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=json.dumps(trust_policy),
            Description='Role for Bedrock Agent Lambda function'
        )
        role_arn = role_response['Role']['Arn']
        
        # Attach policies
        iam_client.attach_role_policy(
            RoleName=role_name,
            PolicyArn='arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole'
        )
        
        iam_client.attach_role_policy(
            RoleName=role_name,
            PolicyArn='arn:aws:iam::aws:policy/AmazonBedrockFullAccess'
        )
        
        # Wait for role to be ready
        print("⏳ Waiting for IAM role to be ready...")
        time.sleep(10)
    
    # Read the deployment package
    with open(package_path, 'rb') as f:
        zip_content = f.read()
    
    # Create or update Lambda function
    function_name = 'BedrockConstitutionAgent'
    
    try:
        # Try to update existing function
        print("🔄 Updating existing Lambda function...")
        lambda_client.update_function_code(
            FunctionName=function_name,
            ZipFile=zip_content
        )
        print(f"✅ Lambda function updated: {function_name}")
    except lambda_client.exceptions.ResourceNotFoundException:
        # Create new function
        print("🆕 Creating new Lambda function...")
        lambda_client.create_function(
            FunctionName=function_name,
            Runtime='python3.9',
            Role=role_arn,
            Handler='lambda_function.lambda_handler',
            Code={'ZipFile': zip_content},
            Description='Lambda function for Bedrock Constitution Agent',
            Timeout=30,
            MemorySize=512
        )
        print(f"✅ Lambda function created: {function_name}")
    
    # Get function ARN
    function_response = lambda_client.get_function(FunctionName=function_name)
    function_arn = function_response['Configuration']['FunctionArn']
    
    print(f"📋 Function ARN: {function_arn}")
    return function_arn

def create_api_gateway():
    """Create API Gateway for Lambda function"""
    print("🌐 Creating API Gateway...")
    
    api_client = boto3.client('apigateway', region_name='us-east-1')
    
    # Create REST API
    api_response = api_client.create_rest_api(
        name='BedrockConstitutionAgentAPI',
        description='API Gateway for Bedrock Constitution Agent',
        endpointConfiguration={'types': ['REGIONAL']}
    )
    api_id = api_response['id']
    print(f"✅ API Gateway created: {api_id}")
    
    # Get root resource
    resources = api_client.get_resources(restApiId=api_id)
    root_resource_id = resources['items'][0]['id']
    
    # Create /chat resource
    chat_resource = api_client.create_resource(
        restApiId=api_id,
        parentId=root_resource_id,
        pathPart='chat'
    )
    chat_resource_id = chat_resource['id']
    
    # Create POST method
    api_client.put_method(
        restApiId=api_id,
        resourceId=chat_resource_id,
        httpMethod='POST',
        authorizationType='NONE'
    )
    
    # Get Lambda function ARN
    lambda_client = boto3.client('lambda', region_name='us-east-1')
    function_name = 'BedrockConstitutionAgent'
    function_response = lambda_client.get_function(FunctionName=function_name)
    function_arn = function_response['Configuration']['FunctionArn']
    
    # Set up integration
    api_client.put_integration(
        restApiId=api_id,
        resourceId=chat_resource_id,
        httpMethod='POST',
        type='AWS_PROXY',
        integrationHttpMethod='POST',
        uri=f'arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/{function_arn}/invocations'
    )
    
    # Add CORS
    api_client.put_method_response(
        restApiId=api_id,
        resourceId=chat_resource_id,
        httpMethod='POST',
        statusCode='200',
        responseParameters={
            'method.response.header.Access-Control-Allow-Origin': True,
            'method.response.header.Access-Control-Allow-Headers': True,
            'method.response.header.Access-Control-Allow-Methods': True
        }
    )
    
    # Deploy API
    deployment = api_client.create_deployment(
        restApiId=api_id,
        stageName='prod',
        description='Production deployment'
    )
    
    # Get API URL
    api_url = f"https://{api_id}.execute-api.us-east-1.amazonaws.com/prod"
    print(f"🌐 API Gateway URL: {api_url}")
    
    return api_url

def main():
    """Main deployment function"""
    print("🚀 Deploying Bedrock Constitution Agent Lambda")
    print("=" * 50)
    
    try:
        # Create Lambda function
        function_arn = create_lambda_function()
        
        # Create API Gateway
        api_url = create_api_gateway()
        
        print("\n🎉 Deployment Complete!")
        print(f"📋 Lambda Function: {function_arn}")
        print(f"🌐 API Gateway URL: {api_url}")
        print(f"🔗 Chat Endpoint: {api_url}/chat")
        
        # Save configuration
        config = {
            'lambda_function_arn': function_arn,
            'api_gateway_url': api_url,
            'chat_endpoint': f"{api_url}/chat"
        }
        
        with open('lambda_agent_config.json', 'w') as f:
            json.dump(config, f, indent=2)
        
        print("\n📁 Configuration saved to: lambda_agent_config.json")
        
    except Exception as e:
        print(f"❌ Deployment failed: {e}")
        return False
    
    return True

if __name__ == "__main__":
    main()
