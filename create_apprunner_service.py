#!/usr/bin/env python3
"""
Create App Runner service using the ECR image
"""

import boto3
import json
import time

AWS_REGION = 'us-east-1'
ACCOUNT_ID = '047719663270'
SERVICE_NAME = 'xperiai-app'
ECR_IMAGE_URI = f'{ACCOUNT_ID}.dkr.ecr.{AWS_REGION}.amazonaws.com/xperiai-app:latest'

def create_iam_role():
    """Create IAM role for App Runner"""
    print("Creating IAM role for App Runner...")
    
    iam = boto3.client('iam', region_name=AWS_REGION)
    role_name = 'AppRunnerXperiaiRole'
    
    trust_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "build.apprunner.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            },
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "tasks.apprunner.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }
    
    # Create role
    try:
        iam.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=json.dumps(trust_policy),
            Description='IAM role for XperiAI App Runner service'
        )
        print(f"[OK] Created role: {role_name}")
    except iam.exceptions.EntityAlreadyExistsException:
        print(f"[OK] Role already exists: {role_name}")
    
    # Attach policies
    print("Attaching policies...")
    
    policies_to_attach = [
        'AmazonBedrockFullAccess',
        'AWSLambda_FullAccess',
        'AmazonS3FullAccess'
    ]
    
    for policy in policies_to_attach:
        try:
            iam.attach_role_policy(
                RoleName=role_name,
                PolicyArn=f'arn:aws:iam::aws:policy/{policy}'
            )
            print(f"[OK] Attached policy: {policy}")
        except Exception as e:
            print(f"[WARNING] Could not attach {policy}: {e}")
    
    role_arn = f'arn:aws:iam::{ACCOUNT_ID}:role/{role_name}'
    return role_arn

def create_apprunner_service():
    """Create App Runner service"""
    print("\nCreating App Runner service...")
    
    apprunner = boto3.client('apprunner', region_name=AWS_REGION)
    
    # Get IAM role ARN
    role_arn = create_iam_role()
    
    service_config = {
        'ServiceName': SERVICE_NAME,
        'SourceConfiguration': {
            'ImageRepository': {
                'ImageIdentifier': ECR_IMAGE_URI,
                'ImageConfiguration': {
                    'Port': '8000',
                    'RuntimeEnvironmentVariables': {
                        'AWS_DEFAULT_REGION': AWS_REGION
                    }
                },
                'ImageRepositoryType': 'ECR'
            },
            'AutoDeploymentsEnabled': True
        },
        'InstanceConfiguration': {
            'Cpu': '1024',
            'Memory': '2048',
            'InstanceRoleArn': role_arn
        }
    }
    
    try:
        response = apprunner.create_service(**service_config)
        
        print("\n" + "="*60)
        print("[SUCCESS] App Runner service created successfully!")
        print("="*60)
        print(f"Service ID: {response['Service']['ServiceId']}")
        print(f"Service Name: {response['Service']['ServiceName']}")
        print(f"Status: {response['Service']['Status']}")
        print("\n[INFO] Service is being deployed...")
        print("       This will take 5-10 minutes.")
        print("\nMonitor progress at:")
        print(f"   https://us-east-1.console.aws.amazon.com/apprunner/home?region=us-east-1#/services/{response['Service']['ServiceId']}")
        print("\n[SUCCESS] Once deployed, you'll get a public URL!")
        print("="*60)
        
        return response['Service']
        
    except Exception as e:
        print(f"\n[ERROR] Error creating App Runner service: {e}")
        print("\nPlease create the service manually using the AWS Console:")
        print("1. Go to App Runner console")
        print("2. Click 'Create service'")
        print("3. Follow the steps in APP_RUNNER_SETUP_INSTRUCTIONS.md")
        raise

if __name__ == '__main__':
    create_apprunner_service()

