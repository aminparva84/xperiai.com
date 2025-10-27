#!/usr/bin/env python3
"""
Deploy Flask app to AWS ECR and App Runner
"""

import boto3
import subprocess
import os
import json

# Configuration
AWS_REGION = 'us-east-1'
ECR_REPO_NAME = 'xperiai-app'
IMAGE_TAG = 'latest'

def create_ecr_repo():
    """Create ECR repository if it doesn't exist"""
    print("🔍 Checking for ECR repository...")
    
    ecr = boto3.client('ecr', region_name=AWS_REGION)
    
    try:
        response = ecr.describe_repositories(repositoryNames=[ECR_REPO_NAME])
        print(f"✅ ECR repository already exists: {ECR_REPO_NAME}")
        return response['repositories'][0]['repositoryUri']
    except ecr.exceptions.RepositoryNotFoundException:
        print("📦 Creating ECR repository...")
        response = ecr.create_repository(
            repositoryName=ECR_REPO_NAME,
            imageScanningConfiguration={'scanOnPush': True}
        )
        repo_uri = response['repository']['repositoryUri']
        print(f"✅ Created ECR repository: {repo_uri}")
        return repo_uri

def build_and_push_image(repo_uri):
    """Build Docker image and push to ECR"""
    print("\n🏗️  Building Docker image...")
    
    # Login to ECR
    print("🔐 Logging in to ECR...")
    subprocess.run([
        'aws', 'ecr', 'get-login-password', '--region', AWS_REGION
    ], check=True)
    
    cmd = f'aws ecr get-login-password --region {AWS_REGION} | docker login --username AWS --password-stdin {repo_uri.split("/")[0]}'
    subprocess.run(cmd, shell=True, check=True)
    
    # Build image
    image_uri = f"{repo_uri}:{IMAGE_TAG}"
    print(f"📦 Building image: {image_uri}")
    subprocess.run([
        'docker', 'build', '-t', image_uri, '.'
    ], check=True)
    
    # Push image
    print(f"🚀 Pushing image to ECR...")
    subprocess.run([
        'docker', 'push', image_uri
    ], check=True)
    
    print(f"✅ Image pushed successfully!")
    return image_uri

def create_apprunner_config():
    """Create apprunner.yaml configuration"""
    config = {
        'version': '1.0',
        'runtime': 'python311',
        'build': {
            'commands': {
                'pre_build': [
                    'pip install --upgrade pip',
                    'pip install -r requirements.txt'
                ]
            }
        },
        'run': {
            'runtime': 'python311',
            'command': 'gunicorn app:app --bind 0.0.0.0:8000 --workers 2 --threads 4 --timeout 120',
            'environment': {
                'AWS_DEFAULT_REGION': AWS_REGION
            }
        }
    }
    
    with open('apprunner.yaml', 'w') as f:
        import yaml
        yaml.dump(config, f)
    
    print("✅ Created apprunner.yaml")

def print_deployment_instructions(image_uri, repo_uri):
    """Print instructions for App Runner deployment"""
    print("\n" + "="*60)
    print("🎉 Docker Image Deployed to ECR!")
    print("="*60)
    print(f"📦 Repository URI: {repo_uri}")
    print(f"🏷️  Image URI: {image_uri}")
    print("\n📋 Next Steps to Deploy to App Runner:")
    print("\n1. Go to AWS Console: https://us-east-1.console.aws.amazon.com/apprunner")
    print("\n2. Click 'Create service'")
    print("\n3. Choose 'Container registry'")
    print(f"\n4. Select ECR and choose repository: {ECR_REPO_NAME}")
    print("\n5. Select the latest image")
    print("\n6. Configure service:")
    print("   - Service name: xperiai-app")
    print("   - Port: 8000")
    print("   - Environment: AWS_DEFAULT_REGION=us-east-1")
    print("\n7. Create IAM role with these permissions:")
    print("   - bedrock:InvokeModel")
    print("   - bedrock:InvokeAgent")
    print("   - lambda:InvokeFunction")
    print("   - s3:GetObject")
    print("   - s3:ListBucket")
    print("\n8. Deploy!")
    print("\n" + "="*60)

def main():
    print("🚀 Deploying to AWS ECR for App Runner")
    print("="*60)
    
    # Create ECR repository
    repo_uri = create_ecr_repo()
    
    # Build and push image
    image_uri = build_and_push_image(repo_uri)
    
    # Create config
    create_apprunner_config()
    
    # Print instructions
    print_deployment_instructions(image_uri, repo_uri)

if __name__ == '__main__':
    main()



