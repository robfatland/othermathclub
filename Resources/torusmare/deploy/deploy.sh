#!/usr/bin/env bash
# Torus Mare - Lambda Deployment Script
# ======================================
# Zips the server/ folder and uploads to AWS Lambda.
#
# Usage:
#   cd torusmare/deploy
#   bash deploy.sh
#
# Prerequisites:
#   - AWS CLI configured (profile: u0027)
#   - Lambda function already created in AWS console or via CLI
#
# Configuration — update these for your environment:
FUNCTION_NAME="torusmare"
AWS_PROFILE="u0027"
REGION="us-west-2"
ZIP_FILE="torusmare_lambda.zip"

# Navigate to server directory
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SERVER_DIR="$SCRIPT_DIR/../server"

echo "Packaging Lambda from: $SERVER_DIR"

# Create the zip (overwrite if exists)
cd "$SERVER_DIR" || exit 1
zip -r "$SCRIPT_DIR/$ZIP_FILE" . -x "*.pyc" "__pycache__/*"

echo "Created: $SCRIPT_DIR/$ZIP_FILE"

# Upload to Lambda
echo "Deploying to Lambda function: $FUNCTION_NAME"
aws lambda update-function-code \
    --function-name "$FUNCTION_NAME" \
    --zip-file "fileb://$SCRIPT_DIR/$ZIP_FILE" \
    --profile "$AWS_PROFILE" \
    --region "$REGION"

echo "Done."
