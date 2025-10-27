
# AWS Bedrock Constitution Expert Agent Setup Guide

## Prerequisites
1. AWS Account with Bedrock access
2. S3 bucket for Constitution documents
3. OpenSearch Serverless collection
4. Proper IAM roles and permissions

## Step 1: Prepare Constitution Documents
1. Download Constitution PDFs to PDFConst/ folder
2. Upload PDFs to S3 bucket: constitution-documents-bucket
3. Organize by folders: constitution/, amendments/, federalist-papers/

## Step 2: Create IAM Roles
Create these IAM roles with appropriate policies:

### BedrockAgentRole
- BedrockAgentServiceRole
- BedrockAgentInvokeModel permissions

### BedrockKnowledgeBaseRole  
- BedrockKnowledgeBaseServiceRole
- S3 read permissions for document bucket
- OpenSearch Serverless permissions

### BedrockDataSourceRole
- S3 read permissions
- Bedrock knowledge base permissions

## Step 3: Set up OpenSearch Serverless
1. Create collection: constitution-collection
2. Configure vector index: constitution-vector-index
3. Set up field mappings for vector, text, and metadata

## Step 4: Create Knowledge Base
1. Use the configuration in bedrock_agent_config.json
2. Connect to S3 data source
3. Configure vector ingestion
4. Set up chunking strategy (1000 tokens, 20% overlap)

## Step 5: Create Bedrock Agent
1. Use ConstitutionExpert configuration
2. Connect to knowledge base
3. Configure with Claude 3 Sonnet
4. Set up specialized instructions

## Step 6: Test the Agent
Test with questions like:
- "What does the First Amendment say?"
- "Explain the 14th Amendment"
- "What is the Commerce Clause?"
- "How does the Constitution define federal powers?"

## Integration with Website
1. Update chat backend to use Constitution agent
2. Add Constitution-specific chat interface
3. Configure routing for Constitutional questions
