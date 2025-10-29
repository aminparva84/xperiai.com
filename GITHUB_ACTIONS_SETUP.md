# 🚀 GitHub Actions Setup for AWS App Runner Deployment

## 📋 Prerequisites

1. **GitHub Repository** with your code
2. **AWS Account** with appropriate permissions
3. **AWS CLI** configured locally (for initial setup)

## 🔐 Required GitHub Secrets

You need to add these secrets to your GitHub repository:

### 1. Go to GitHub Repository Settings
- Navigate to your repository on GitHub
- Click **Settings** tab
- Click **Secrets and variables** → **Actions**
- Click **New repository secret**

### 2. Add Required Secrets

| Secret Name | Description | Example Value |
|-------------|-------------|---------------|
| `AWS_ACCESS_KEY_ID` | AWS Access Key ID | `AKIA...` |
| `AWS_SECRET_ACCESS_KEY` | AWS Secret Access Key | `[Your Secret Key]` |

## 🏗️ AWS Resources Setup

### 1. Create ECR Repository (if not exists)
```bash
aws ecr create-repository \
  --repository-name xperiai-app \
  --region us-east-1 \
  --image-scanning-configuration scanOnPush=true
```

### 2. Create IAM User for GitHub Actions
```bash
# Create IAM user
aws iam create-user --user-name github-actions-xperiai

# Create access key
aws iam create-access-key --user-name github-actions-xperiai

# Attach policies
aws iam attach-user-policy \
  --user-name github-actions-xperiai \
  --policy-arn arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryFullAccess

aws iam attach-user-policy \
  --user-name github-actions-xperiai \
  --policy-arn arn:aws:iam::aws:policy/AppRunnerFullAccess
```

### 3. App Runner Service Configuration
Your App Runner service should be configured to:
- **Source**: Container registry (ECR)
- **Repository**: `xperiai-app`
- **Tag**: `latest`
- **Auto-deploy**: Enabled

## 🔄 Workflow Configuration

The GitHub Actions workflow (`/.github/workflows/deploy-apprunner.yml`) will:

1. **Trigger**: On push to `main` branch or manual dispatch
2. **Build**: Docker image with your application
3. **Push**: Image to ECR with commit SHA and `latest` tags
4. **Deploy**: App Runner automatically pulls the new image
5. **Verify**: Check deployment status and provide URL

## 🚀 Deployment Process

### Automatic Deployment
1. Push code to `main` branch
2. GitHub Actions automatically:
   - Builds Docker image
   - Pushes to ECR
   - App Runner detects new image
   - Deploys automatically

### Manual Deployment
1. Go to **Actions** tab in GitHub
2. Select **Deploy Xperi AI to AWS App Runner**
3. Click **Run workflow**
4. Select branch and click **Run workflow**

## 📊 Monitoring Deployment

### GitHub Actions Logs
- Go to **Actions** tab
- Click on the latest workflow run
- View detailed logs for each step

### AWS App Runner Console
- Navigate to AWS App Runner service
- View service status and logs
- Monitor deployment progress

## 🔧 Troubleshooting

### Common Issues

1. **ECR Repository Not Found**
   - The workflow will create it automatically
   - Or create manually: `aws ecr create-repository --repository-name xperiai-app`

2. **Permission Denied**
   - Check AWS credentials in GitHub secrets
   - Verify IAM user has required permissions

3. **App Runner Service Not Found**
   - Verify service ARN in workflow
   - Check if service exists in AWS console

4. **Build Failures**
   - Check Dockerfile syntax
   - Verify all dependencies in requirements.txt
   - Check GitHub Actions logs for specific errors

### Debug Commands
```bash
# Check ECR repositories
aws ecr describe-repositories --region us-east-1

# Check App Runner services
aws apprunner list-services --region us-east-1

# Check specific service
aws apprunner describe-service \
  --service-arn arn:aws:apprunner:us-east-1:047719663270:service/xperiai-app/a706b799597740b698a471a2dc613568 \
  --region us-east-1
```

## 🎯 Expected Results

After successful deployment:
- ✅ Docker image pushed to ECR
- ✅ App Runner service updated
- ✅ Application accessible via App Runner URL
- ✅ New templated responses working

## 📱 Your App URLs

Once deployed, your application will be available at:
- **Main App**: `https://qaptibvncn.us-east-1.awsapprunner.com`
- **Chat Interface**: `https://qaptibvncn.us-east-1.awsapprunner.com/chat`
- **Admin Dashboard**: `https://qaptibvncn.us-east-1.awsapprunner.com/admin`

## 🔄 Next Steps

1. **Add GitHub Secrets** (AWS credentials)
2. **Push to main branch** to trigger deployment
3. **Monitor deployment** in GitHub Actions
4. **Test your application** with new templated responses
5. **Set up monitoring** and alerts as needed

---

**🎉 Your automated deployment pipeline is ready!**
