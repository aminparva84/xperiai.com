# Quick Deploy Steps

## 🚀 **After Installing Docker:**

```powershell
# 1. Create ECR repo
aws ecr create-repository --repository-name xperiai-app --region us-east-1

# 2. Login to ECR (replace YOUR_ACCOUNT_ID)
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com

# 3. Build image
docker build -t xperiai-app .

# 4. Get ECR URI
$ECR_URI = aws ecr describe-repositories --repository-names xperiai-app --region us-east-1 --query "repositories[0].repositoryUri" --output text

# 5. Tag image
docker tag xperiai-app:latest "$ECR_URI:latest"

# 6. Push image
docker push "$ECR_URI:latest"

# 7. Go to App Runner console and create service
start https://us-east-1.console.aws.amazon.com/apprunner
```

## ✅ **Then in AWS Console:**

Follow steps in `DEPLOY_TO_APP_RUNNER.md` to create the App Runner service.



