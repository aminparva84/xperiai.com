# 🚀 App Runner Setup Instructions

Your Docker image has been successfully pushed to ECR!

## ✅ **What's Done:**
- ✅ ECR repository created: `xperiai-app`
- ✅ Docker image built and pushed
- ✅ Image URI: `047719663270.dkr.ecr.us-east-1.amazonaws.com/xperiai-app:latest`

## 📋 **Now Create App Runner Service:**

### **Step 1: Go to App Runner Console**
Open: https://us-east-1.console.aws.amazon.com/apprunner

### **Step 2: Click "Create service"**

### **Step 3: Choose Source**
- Select: **Container registry**
- Choose: **Amazon ECR**
- Repository: Select `xperiai-app`
- Tag: Select `latest`

### **Step 4: Configure Service**
Click "Next"

**Deployment settings:**
- Service name: `xperiai-app`
- Port: `8000`
- Start command: (leave empty - uses CMD from Dockerfile)
- Health check path: `/` (optional)

### **Step 5: Configure Environment**
Add environment variable:
- Key: `AWS_DEFAULT_REGION`
- Value: `us-east-1`

### **Step 6: Create IAM Role**

**Create new role:**

**Role name:** `AppRunnerXperiaiRole`

**Attach policies:**
1. Custom policy with this JSON:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeAgent",
        "bedrock-runtime:InvokeModel",
        "bedrock-runtime:InvokeAgent"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "lambda:InvokeFunction"
      ],
      "Resource": "arn:aws:lambda:us-east-1:047719663270:function:BedrockConstitutionAgent"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::constitution-knowledge-base-2024",
        "arn:aws:s3:::constitution-knowledge-base-2024/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": "ecr:GetAuthorizationToken",
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ecr:BatchCheckLayerAvailability",
        "ecr:GetDownloadUrlForLayer",
        "ecr:BatchGetImage"
      ],
      "Resource": "arn:aws:ecr:us-east-1:047719663270:repository/xperiai-app"
    }
  ]
}
```

Or use Amazon managed policies:
- `AmazonBedrockFullAccess`
- `AWSLambda_FullAccess`
- `AmazonS3FullAccess`

### **Step 7: Configure Auto Scaling**
- Min instances: 1
- Max instances: 5
- Concurrency: 100 requests per instance

### **Step 8: Review and Create**
Click **"Create & deploy"**

### **Step 9: Wait for Deployment**
This will take 5-10 minutes. Monitor the deployment in the console.

### **Step 10: Get Your URL**
Once deployed, you'll get a URL like:
`https://abc123xyz.us-east-1.awsapprunner.com`

Test your app:
- Home: `https://YOUR-URL.awsapprunner.com/`
- Chat: `https://YOUR-URL.awsapprunner.com/chat`

## 🎉 **Done!**

Your app is now live on AWS App Runner! 🚀

