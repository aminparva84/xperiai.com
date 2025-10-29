# Easy AWS Cleanup Guide - Keep Only S3, Bedrock, ECR, App Runner

## ✅ What to KEEP in us-east-1

1. **S3** - Your storage buckets
2. **Bedrock** - Your AI agent API
3. **ECR** - Container registry (`xperiai-app`)
4. **App Runner** - Your deployed service (`xperiai-app`)

## ❌ What to DISABLE (All Regions)

- EC2 Instances
- VPCs (except default)
- Lambda Functions (except `BedrockConstitutionAgent` in us-east-1 if needed)
- Load Balancers
- RDS Databases
- ECS/EKS Clusters
- Redshift Clusters
- ElastiCache Clusters
- Everything in regions other than us-east-1

## 🔧 How to Clean Up

### Option 1: Use the Python Script (When AWS Credentials Configured)

```bash
python cleanup_aws_resources.py
```

This will:
- Scan all AWS regions
- List all resources
- Generate commands to disable/delete them
- Save commands to `disable_resources_commands.sh`

### Option 2: Use AWS Console (Recommended - Safe & Visual)

#### Step 1: EC2 Console
1. Go to: https://console.aws.amazon.com/ec2/
2. Select **each region** (dropdown at top)
3. For each region:
   - **EC2 Instances**: Select all → Actions → Instance State → Stop/Terminate
   - **VPCs**: Select non-default VPCs → Delete VPC (careful - delete dependencies first!)

#### Step 2: Lambda Console
1. Go to: https://console.aws.amazon.com/lambda/
2. Select **each region** (dropdown at top)
3. For each Lambda function (except `BedrockConstitutionAgent` in us-east-1):
   - Select function → Actions → Delete

#### Step 3: RDS Console
1. Go to: https://console.aws.amazon.com/rds/
2. Select **each region**
3. For each database:
   - Select → Actions → Delete (backup first if needed!)

#### Step 4: Load Balancer Console
1. Go to: https://console.aws.amazon.com/ec2/home#LoadBalancers:
2. Select **each region**
3. Delete all load balancers

#### Step 5: Other Services
- **ECS**: https://console.aws.amazon.com/ecs/
- **EKS**: https://console.aws.amazon.com/eks/
- **Redshift**: https://console.aws.amazon.com/redshift/
- **ElastiCache**: https://console.aws.amazon.com/elasticache/

### Option 3: Quick Region Cleanup

For each region (except us-east-1):
1. Go to AWS Console
2. Select region from dropdown
3. Use Resource Groups & Tag Editor
4. View resources by region
5. Delete unwanted resources

## 💰 Expected Cost Savings

**Before cleanup:**
- EC2 instances: $10-100+/month per instance
- RDS databases: $15-100+/month per database
- Load balancers: $16-25/month per load balancer
- Other services: Varies

**After cleanup (keeping only essentials):**
- App Runner: ~$7-15/month
- ECR: ~$0.10/month
- S3: ~$0.023/GB (minimal)
- Bedrock: Pay-per-use ($0 when idle)

**Total: ~$7-20/month** instead of potentially $100+/month

## ⚠️ Important Warnings

1. **VPC Deletion**: VPCs have dependencies (subnets, gateways, etc.). Delete in this order:
   - Delete instances in VPC
   - Delete load balancers
   - Delete NAT gateways
   - Delete internet gateways (detach first)
   - Delete subnets
   - Delete route tables
   - Delete security groups
   - Delete VPC

2. **Lambda Function**: Keep `BedrockConstitutionAgent` in us-east-1 if your App Runner uses it

3. **S3 Buckets**: Keep only buckets related to your project. Check bucket contents before deleting.

4. **Backup First**: If you have any important data, backup before deleting RDS, EBS volumes, etc.

## 📋 Quick Checklist

- [ ] Check EC2 instances in all regions → Stop/Terminate
- [ ] Check VPCs in all regions → Delete (carefully!)
- [ ] Check Lambda functions → Delete (except BedrockConstitutionAgent in us-east-1)
- [ ] Check RDS instances → Delete (backup first!)
- [ ] Check Load Balancers → Delete
- [ ] Check ECS/EKS clusters → Delete
- [ ] Check Redshift → Delete
- [ ] Check ElastiCache → Delete
- [ ] Verify S3, Bedrock, ECR, App Runner still running in us-east-1

## 🎯 Verification

After cleanup, verify these are still running in us-east-1:
- ✅ App Runner service: `xperiai-app`
- ✅ ECR repository: `xperiai-app`
- ✅ Bedrock API access (try making a test call)
- ✅ S3 buckets (if you have project-related buckets)

## 📊 Cost Monitoring

After cleanup, monitor costs in:
- AWS Cost Explorer: https://console.aws.amazon.com/cost-management/home#/
- Set up billing alerts to get notified of unexpected charges

