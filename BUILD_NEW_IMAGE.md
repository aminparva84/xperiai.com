# Build New Docker Image via GitHub Actions

## ✅ What's Ready

Your GitHub Actions workflow is configured to:
1. **Build Docker image** from your code
2. **Push to ECR** (Elastic Container Registry)
3. **Auto-deploy** to App Runner (since auto-deploy is enabled)

## 🚀 How to Build a New Image

### Option 1: Helper Push to Main Branch (Automatic)

```bash
# Add your changes
git add .

# Commit changes
git commit -m "Fix App Runner deployment and add missing redirect import"

# Push to main branch
git push origin main
```

This will **automatically trigger** the GitHub Actions workflow!

### Option 2: Manual Workflow Trigger (No Code Push Needed)

1. Go to your GitHub repository: https://github.com/aminparva84/xperiai.com
2. Click红 **Actions** tab
3. Select **"Deploy Xperi AI to AWS App Runner"** workflow
4. Click **"Run workflow"** button (top right)
5. Select branch: **`main`** (or your branch)
6. Click **"Run workflow"**

## 📋 What the Workflow Does

1. **Checks out your code**
2. **Configures AWS credentials** (from GitHub secrets)
3. **Creates ECR repository** (if it doesn't exist)
4. **Builds Docker image** with your latest code
5. **Tags image** with commit SHA and `latest`
6. **Pushes to ECR**:
   - `047719663270.dkr.ecr.us-east-1.amazonaws.com/xperiai-app:<commit-sha>`
   - `047719663270.dkr.ecr.us-east-1.amazonaws.com/xperiai-app:latest`
7. **App Runner automatically detects** the new `latest` tag
8. **App Runner deploys** the new image (takes 5-10 minutes)

## ✅ Recent Fixes Applied

- ✅ Added missing `redirect` import in `app.py` (this was causing App Runner to fail!)
- ✅ Updated GitHub Actions workflow to tag images properly
- ✅ Added ECR repository auto-creation

## 🔍 Monitor the Build

1. **GitHub Actions Tab**: Watch the build progress
   - Build: ~2-5 minutes
   - Push to ECR: ~1-2 minutes
   - App Runner deployment: ~5-10 minutes

2. **App Runner Console**: Check deployment status
   - https://us-east-1.console.aws.amazon.com/apprunner/home?region=us-east-1#/services/xperiai-app

3. **Your App URL**: Test when ready
   - https://qaptibvncn.us-east-1.awsapprunner.com

## 🐛 Troubleshooting

### If Build Fails:
- Check GitHub Actions logs for errors
- Verify AWS credentials in GitHub secrets
- Ensure Dockerfile is correct

### If App Runner Doesn't Update:
- App Runner checks for new images every few minutes
- Wait 5-10 minutes after image is pushed
- Check App Runner logs in AWS Console
- Verify auto-deploy is enabled in App Runner service

### If App Still Not Working:
- Check App Runner logs: https://us-east-1.console.aws.amazon.com/apprunner/home?region=us-east-1#/services/xperiai-app/logs
- Verify health check endpoint: `/chat/health`
- Check that port 8000 is correct in Dockerfile

## 🎯 Next Steps

1. **Commit and push your fixes** (or trigger workflow manually)
2. **Watch GitHub Actions** build the image
3. **Wait for App Runner** to deploy (5-10 minutes)
4. **Test your app** at the App Runner URL
5. **Check logs** if there are any issues

## 📊 Expected Timeline

```
Git Push → GitHub Actions → Build Image → Push to ECR → App Runner Deploy → Live
  1 min       2-5 min         1-2 min        5-10 min        Ready!
```

Total time: ~10-20 minutes from push to live deployment

