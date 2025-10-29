# Quick AWS Cost Check - What to Keep/Disable

## ✅ KEEP (Essential - 3 Services)

### 1. **App Runner** - `xperiai-app`
   - **Location:** https://us-east-1.console.aws.amazon.com/apprunner/home?region=us-east-1
   - **Cost:** ~$7-15/month
   - **Status:** KEEP ✓
   
### 2. **ECR Repository** - `xperiai-app`
   - **Location:** https://us-east-1.console.aws.amazon.com/ecr/repositories?region=us-east-1
   - **Cost:** ~$0.10/month per GB
   - **Status:** KEEP ✓

### 3. **Bedrock API** (Pay-per-use)
   - **Location:** https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1
   - **Cost:** $0 when not in use, pay-per-use when called
   - **Status:** KEEP ✓

## ⚠️ CHECK & POSSIBLY DISABLE

### 4. **Lambda Function** - `BedrockConstitutionAgent`
   - **Location:** https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1
   - **Cost:** Free tier (1M/month), then $0.20/1M requests
   - **Status:** CHECK ⚠️
   - **Action:** Your code uses this, but you could refactor to call Bedrock directly

### 5. **S3 Buckets** (for knowledge base)
   - **Location:** https://s3.console.aws.amazon.com/s3/buckets?region=us-east-1
   - **Look for:** buckets with "constitution", "bedrock", "xperiai" in name
   - **Cost:** ~$0.023/GB + transfer
   - **Status:** CHECK ⚠️ - Disable if not using knowledge bases

### 6. **Bedrock Knowledge Bases**
   - **Location:** https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1#/agents
   - **Cost:** Depends on OpenSearch usage
   - **Status:** CHECK ⚠️ - Disable if not using RAG

### 7. **OpenSearch Collections** ⚠️ MOST EXPENSIVE!
   - **Location:** https://us-east-1.console.aws.amazon.com/aos/home?region=us-east-1#opensearch/collections
   - **Cost:** ~$0.25/hour = **~$180/month if running 24/7**
   - **Status:** DISABLE ✗ - Unless you're actively using knowledge bases
   - **Action:** Check this FIRST - biggest cost saver!

## 💰 Cost Breakdown

**Minimum (Keep essential only):**
- App Runner: $7-15/month
- ECR: $0.10/month
- Bedrock: Pay-per-use (varies)
- **Total: ~$7-15/month**

**If依存 on the extras:**
- Lambda: Free (within tier)
- S3: $0.50-5/month (if storing data)
- OpenSearch: **$180/month** (if 24/7) ⚠️
- **Total: ~$200+/month**

## 🎯 Quick Actions

### Step 1: Check OpenSearch (Highest Priority!)
1. Go to OpenSearch console
2. **If collections exist and you're not using knowledge bases → DELETE**
3. **This can save ~$180/month**

### Step 2: Check S3 Buckets
1. Go to S3 console
2. Look for project-related buckets
3. **If not using knowledge bases → DELETE**

### Step 3: Check Lambda Usage
1. Go to Lambda console
2. Check `BedrockConstitutionAgent` invocations
3. **If using, keep it (free tier)**
4. **Consider refactoring later to remove Lambda**

### Step 4: Check Bedrock Knowledge Bases
1. Go to Bedrock console → Agents
2. **If knowledge bases exist and not using → DELETE**

## ✅ Final Recommendation

**KEEP (3 services):**
1. ✓ App Runner
2. ✓ ECR  
3. ✓ Bedrock API

**DISABLE (if not using):**
1. ✗ OpenSearch Collections (check this first!)
2. ✗ S3 Buckets (for knowledge base)
3. ✗ Bedrock Knowledge Bases (if not using RAG)

**CHECK:**
- Lambda - You're using it, so keep for now (free tier)

## 📊 To Check Your Actual Costs

Go to: https://console.aws.amazon.com/cost-management/home

Filter by service to see breakdown of:
- App Runner costs
- Lambda costs
- S3 costs
- OpenSearch costs (if any)

