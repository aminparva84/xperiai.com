# Setup GitHub Actions for Automatic Deployment

## ✅ What We Created

A GitHub Actions workflow that automatically builds and deploys your Docker image to AWS App Runner whenever you push to the `main` branch.

## 🔧 Setup Steps

### Step 1: Add AWS Credentials to GitHub Secrets

1. Go to your repository: https://github.com/aminparva84/xperiai.com
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add these secrets:

**Secret 1:**
- Name: `AWS_ACCESS_KEY_ID`
- Value: (Add your access key from AWS console)

**Secret 2:**
- Name: `AWS_SECRET_ACCESS_KEY`
- Value: (Add your secret key from AWS console)

### Step 2: Commit and Push

```powershell
git add .
git commit -m "Add GitHub Actions workflow for App Runner deployment"
git push origin main
```

### Step 3: Watch It Deploy

1. Go to **Actions** tab in your repository
2. Click on the running workflow
3. Watch it build and deploy automatically!

## 🚀 How It Works

1. **Trigger:** Push to `main` branch
2. **Build:** Docker image is built using the Dockerfile
3. **Push:** Image is pushed to ECR
4. **Deploy:** App Runner automatically detects new image and deploys (since auto-deploy is enabled)

## 📝 Workflow File

The workflow is in: `.github/workflows/deploy-apprunner.yml`

It does:
- ✅ Checkout your code
- ✅ Configure AWS credentials
- ✅ Login to ECR
- ✅ Build Docker image
- ✅ Push to ECR
- ✅ Check deployment status

## 🎉 Benefits

- **Automatic:** No manual Docker commands needed
- **Consistent:** Every push gets deployed
- **Fast:** Deploys in ~5-10 minutes
- **CI/CD:** Professional deployment pipeline!

## 🔄 Deploy Again

Just push to main:
```powershell
git add .
git commit -m "Update app"
git push origin main
```

The workflow will automatically build and deploy!

