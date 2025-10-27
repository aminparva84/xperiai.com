# Create App Runner Service - Quick Steps

## ✅ Already Done:
- ECR repository created: `xperiai-app`
- Docker image built and pushed to ECR
- IAM role created: `AppRunnerXperiaiRole` (with all permissions)

## 🚀 Create App Runner Service (Manual):

### Step 1: In AWS App Runner Console
The console should be open. If not, click here:
https://us-east-1.console.aws.amazon.com/apprunner

### Step 2: Click "Create service"

### Step 3: Select Source
- Choose: **Container registry**
- Select: **Amazon ECR**
- Click **"Browse"** and select: **xperiai-app**
- Select: **latest** (image tag)

### Step 4: Configure Deployment
- Click **"Next"**
- Service name: `xperiai-app`
- Configure settings:
  - Deployment trigger: **Automatic** (default)
  - Port: **8000**

### Step 5: Environment Variables
Click **"Add environment variable"**:
- Key: `AWS_DEFAULT_REGION`
- Value: `us-east-1`

### Step 6: Configure Service
- CPU: **0.25 vCPU**
- Memory: **0.5 GB**
- Health check: Leave default

### Step 7: Select IAM Role
- Role: **AppRunnerXperiaiRole** (already created with permissions)

Or if not showing:
- Create new role: **AppRunnerXperiaiRole**
- Attach these managed policies:
  - AmazonBedrockFullAccess
  - AWSLambda_FullAccess
  - AmazonS3FullAccess

### Step 8: Auto Scaling (Optional)
- Min instances: **1**
- Max instances: **5**

### Step 9: Create & Deploy
Click **"Create & deploy"**

### Step 10: Wait
- Deployment takes 5-10 minutes
- Monitor progress in the console
- When complete, you'll get a URL like:
  `https://abc123.us-east-1.awsapprunner.com`

### Step 11: Test Your App
- Home: `https://YOUR-URL.awsapprunner.com/`
- Chat: `https://YOUR-URL.awsapprunner.com/chat`

## 🎉 Done!
Your app is now live on AWS App Runner!

