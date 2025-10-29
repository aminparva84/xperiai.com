# AWS Cost Optimization Guide

## ✅ Keep These Services (Essential for Your Project)

Based on your code analysis, these are REQUIRED:

1. **App Runner** - Your container deployment service
   - Service: `xperiai-app`
   - Cost: ~$7-15/month
   - **KEEP** ✓

2. **ECR (Elastic Container Registry)** - Docker image storage
   - Repository: `xperiai-app`
   - Cost: ~$0.10/month per GB
   - **KEEP** ✓

3. **Bedrock API** - AI agent calls (pay-per-use)
   - Used directly in your code via `boto3.client('bedrock-runtime')`
   - Cost: ~$0.008-0.015 per 1K input tokens
   - **$0 when not in use** - No fixed costs
   - **KEEP** ✓ (It's already pay-per-use)

## ⚠️ Check These Services (May Not Be Needed)

Based on your code, check if these are actually used:

### 1. **Lambda Function** - `BedrockConstitutionAgent`
   - **Your code shows:** App Runner calls Lambda, Lambda calls Bedrock
   - **Alternative:** You could call Bedrock directly from App Runner
   - **Cost:** Free tier (1M requests/month), then $0.20 per 1M requests
   - **Action:** Check if you can refactor to remove Lambda
   - **CHECK** ⚠️

### 2. **S3 Buckets** - For knowledge base storage
   - **Your code shows:** Referenced in setup files but may not be active
   - **Cost:** ~$0.023/GB storage + transfer costs
   - **Action:** Check AWS Console if any S3 buckets exist for this project
   - **CHECK** ⚠️

### 3. **Bedrock Knowledge Bases** - RAG system
   - **Your code shows:** Setup files exist but may not be active
   - **Cost:** Depends on OpenSearch usage
   - **Action:** Check if knowledge bases are actually created and used
   - **CHECK** ⚠️

### 4. **OpenSearch Serverless** - For knowledge base vector search
   - **Your code shows:** Referenced in setup files
   - **Cost:** ~$0.25/hour for collections (can be expensive!)
   - **Action:** **Disable if not using knowledge bases**
   - **DISABLE if not needed** ✗

## 🔍 How to Check What You're Actually Using

### Option 1: Run the Python Script (When AWS Credentials Configured)
```bash
python check_aws_resources.py
```

### Option 2: Check AWS Console Manually

1. **Lambda Functions:**
   - Go to: https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1
   - Check if `BedrockConstitutionAgent` exists
   - Check if it has any invocations/metrics

2. **S3 Buckets:**
   - Go to: https://s3.console.aws.amazon.com/s3/buckets?region=us-east-1
   - Look for buckets with names like: `constitution`, `bedrock`, `xperiai`, `knowledge`
   - Check if they have any data

3. **Bedrock Knowledge Bases:**
   - Go to: https://us-east-1. 버튼console.aws.amazon.com/bedrock/home?region=us-east-1#/agents
   - Check if any knowledge bases exist

4. **OpenSearch Collections:**
   - Go to: https://us-east-1.console.aws.amazon.com/aos/home?region=us-east-1#opensearch/collections
   - Check if any collections exist (these can be expensive!)

## 💰 Current Cost Estimate (Derived from Code)

Based on your configuration:

```
✓ App Runner:        ~$7-15/month (running service)
✓ ECR Storage:       ~$0.10/month (small images)
✓ Bedrock API:       Pay-per-use (varies with usage)
? Lambda:            Free tier up to 1M requests/month
? S3:                Depends on storage ($0.023/GB if exists)
? OpenSearch:        ~$0.25/hour if running (~$180/month if 24/7)

Total if minimal:    ~$7-15/month (App Runner + ECR + Bedrock usage)
Total if all active: ~$200+/month (if OpenSearch is running 24/7)
```

## 🎯 Recommendations

### Immediate Actions:

1. **Verify Lambda Usage:**
   - Check your `app.py` - it calls `BedrockConstitutionAgent` Lambda
   - If this is working, you might need to keep it
   - **However**, you could refactor to call Bedrock directly from App Runner to remove Lambda

2. **Check for OpenSearch Collections:**
   - These are the most expensive if running 24/7
   - If you're not using knowledge bases, **DELETE these immediately**
   - Can save ~$180/month

3. **Check S3 Buckets:**
   - If you have S3 buckets but aren't using knowledge bases, delete them
   - Can save ~$0.50-5/month depending on size

### Code Analysis Shows:

**Your `app.py` shows:**
- ✓ Calls Lambda function `BedrockConstitutionAgent`
- ✓ Lambda then calls Bedrock

**Potential eliminations:**
1. **Remove Lambda middleman** - Call Bedrock directly from App Runner
   - Would save: Free tier is free, but simplifies architecture
   - Requires code refactoring

2. **If not using knowledge bases:**
   - Delete OpenSearch collections (biggest cost saver)
   - Delete S3 buckets used for documents
   - Delete Bedrock knowledge bases

## 📋 Quick Checklist

- [ ] Run `python check_aws_resources.py` (when credentials configured)
- [ ] Check AWS Console for OpenSearch collections (disable if not needed)
- [ ] Check AWS Console for S3 buckets (delete if not needed)
- [ ] Check AWS Console for Lambda invocations (refactor if possible)
- [ ] Verify Bedrock knowledge bases (delete if not using)
- [ ] Keep: App Runner, ECR, Bedrock API

## 🚀 Next Steps

1. **Configure AWS credentials** locally or run script in AWS CloudShell
2. **Run the check script** to see actual resources
3. **Review costs** in AWS Cost Explorer
4. **Disable unused services** based on findings

