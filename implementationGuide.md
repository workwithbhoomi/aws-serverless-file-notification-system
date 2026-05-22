## Step-by-Step Implementation Guide

### Step 1 — Create an S3 Bucket

1. Open AWS Console
2. Search for **S3**
3. Click **Create Bucket**
4. Enter a globally unique bucket name
5. Keep:
   - ACLs disabled
   - Block all public access enabled
6. Leave versioning disabled
7. Keep default encryption settings
8. Click **Create Bucket**

---

### Step 2 — Create Lambda Function

1. Open AWS Console
2. Search for **Lambda**
3. Click **Create Function**
4. Choose:
   - Author from scratch
5. Configure:
   - Function Name: `file-upload-handler`
   - Runtime: Python 3.x
   - Architecture: x86_64
6. Under permissions:
   - Select "Create a new role with basic Lambda permissions"
7. Click **Create Function**

---

### Step 3 — Add Lambda Function Code

Replace the default Lambda code with:

```python
import json
import boto3

sns = boto3.client('sns')

TOPIC_ARN = 'YOUR_SNS_TOPIC_ARN'

def lambda_handler(event, context):

    message = "A new file was uploaded to your S3 bucket."

    sns.publish(
        TopicArn=TOPIC_ARN,
        Message=message,
        Subject='S3 File Upload Alert'
    )

    print("Notification sent successfully!")

    return {
        'statusCode': 200,
        'body': 'Success'
    }
```

Click **Deploy** after updating the code.

---

### Step 4 — Create SNS Topic

1. Open AWS Console
2. Search for **SNS**
3. Click **Create Topic**
4. Choose:
   - Standard Topic
5. Enter topic name:
   - `file-upload-alerts`
6. Click **Create Topic**

---

### Step 5 — Create SNS Subscription

1. Open the created SNS topic
2. Click **Create Subscription**
3. Configure:
   - Protocol: Email
   - Endpoint: Your email address
4. Click **Create Subscription**
5. Confirm the subscription through the email received from AWS

---

### Step 6 — Attach SNS Permission to Lambda Role

1. Open Lambda Function
2. Go to:
   - Configuration → Permissions
3. Click the execution role name
4. Click:
   - Add Permissions → Attach Policies
5. Search and attach:
   - `AmazonSNSFullAccess`

---

### Step 7 — Configure S3 Trigger

1. Open Lambda Function
2. Click **Add Trigger**
3. Select:
   - S3
4. Choose the created bucket
5. Event Type:
   - PUT
6. Acknowledge recursive invocation warning
7. Click **Add**

---

### Step 8 — Test the Workflow

1. Upload a small file into the S3 bucket
2. Verify:
   - Lambda execution triggered
   - CloudWatch logs generated
   - Email notification received through SNS

---

### Step 9 — Monitor Logs Using CloudWatch

1. Open Lambda Function
2. Go to:
   - Monitor → View CloudWatch Logs
3. Verify execution logs and notification status

---

## Final Workflow

```
S3 Bucket
   ↓
Lambda Trigger
   ↓
SNS Notification
   ↓
Email Alert
```