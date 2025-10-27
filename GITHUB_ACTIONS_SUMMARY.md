# GitHub Actions Workflow Created!

## What Was Created

A complete CI/CD pipeline that automatically builds and deploys your app to AWS App Runner whenever you push to GitHub.

## Files Created

1. **`.github/workflows/deploy-apprunner.yml`** - The GitHub Actions workflow
2. **`SETUP_GITHUB_ACTIONS.md`** - Setup instructions

## Next Steps

### 1. Add AWS Secrets to GitHub
Go to: https://github.com/aminparva84/xperiai.com/settings/secrets/actions

Add these secrets (use your AWS credentials):
- `AWS_ACCESS_KEY_ID`: (Your access key)
- `AWS_SECRET_ACCESS_KEY`: (Your secret key)

### 2. Commit and Push

```powershell
git add .
git commit -m "Add GitHub Actions CI/CD pipeline"
git push origin main
```

### 3. Watch It Deploy

Go to: https://github.com/aminparva84/xperiai.com/actions

You'll see the workflow running automatically!

## How It Works

1. You push code to `main` branch
2. GitHub Actions starts
3. Builds Docker image
4. Pushes to ECR
5. App Runner automatically deploys (auto-deploy is enabled)

## Benefits

- ✅ **Automatic deployment** - No manual Docker commands
- ✅ **Consistent builds** - Same process every time  
- ✅ **Fast** - Deploys in 5-10 minutes
- ✅ **Professional** - Industry-standard CI/CD
- ✅ **Free** - GitHub Actions included with your account

## Deploying Updates

Just push your changes:
```powershell
git add .
git commit -m "Update app"
git push origin main
```

The workflow will automatically build and deploy!

