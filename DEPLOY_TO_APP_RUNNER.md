# Deploy to AWS App Runner

## 📋 **Prerequisites:**

1. **Install Docker Desktop:** https://www.docker.com/products/docker-desktop/
2. **AWS CLI configured:** `aws configure`
3. **ECR credentials:** We'll create repository

## 🚀 **Deployment Steps:**

### **Step 1: Install Docker Desktop**

Download and install Docker Desktop for Windows:
https://www.docker.com/products/docker-desktop/

After installation, restart your computer.

### **Step 2: Verify Docker**

```powershell
docker --version
docker ps
```

### **Step 3: Create ECR Repository**

Run this script:
```powershell
python deploy_to_apprunner.py
```

Or manually:
```powershell
aws ecr create-repository --repository-name xperiai-app --region us-east-1
```

Get repository URI:
```powershell
aws ecr describe-repositories --repository-names xperiai-app --region us-east-1
```

### **Step 4: Build and Push Docker Image**

Login to ECR:
```powershell
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com
```

Build image:
```powershell
docker build -t xperiai-app .
```

Tag image:
```powershell
docker tag xperiai-app:latest YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/xperiai-app:latest
```

Push image:
```powershell
docker push YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/xperiai-app:latest
```

### **Step 5: Create App Runner Service**

Go to: https://us-east-1.console.aws.amazon.com/apprunner

1. Click **"Create service"**
2. Choose **"Container registry"** → **"Amazon ECR"**
3. Select repository: **xperiai-app**
4. Select tag: **latest**
5. Click **"Next"**

### **Step 6: Configure Service**

**Service name:** `xperiai-app`

**Deployment settings:**
- Port: `8000`
- Environment variables:
  - `AWS_DEFAULT_REGION` = `us-east-1`

**Auto-deploy:** Yes (recommended)

### **Step 7: Create IAM Role**

**Create new role or use existing:**

**Trust policy:**
```json
{
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
```

**Policy (attach this to role):**
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
    }
  ]
}
```

### **Step 8: Create Service**

Click **"Create & deploy"**

App Runner will:
1. Pull your image from ECR
2. Start the container
3. Provide a URL like: `https://abc123.us-east-1.awsapprunner.com`

### **Step 9: Test**

Your app will be live at the App Runner URL!

Try: `https://YOUR-URL.us-east-1.awsapprunner.com/chat`

## 🔄 **Auto-Update:**

Every time you push a new image to ECR:
1. Go to App Runner service
2. Click **"Rollback"** to update to latest
3. Or set auto-deploy to trigger on new images

## 📊 **Estimated Costs:**

- **App Runner:** ~$7-15/month (low traffic)
- **ECR:** ~$0.10/month (storage)
- **Data transfer:** ~$0.10/GB

**Total:** ~$10-20/month

## 🎯 **Next Steps:**

1. Install Docker Desktop
2. Run: `python deploy_to_apprunner.py`
3. Follow App Runner console steps
4. Enjoy your live app!



