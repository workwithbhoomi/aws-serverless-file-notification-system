# AWS Serverless File Notification System

## Project Overview

This project demonstrates a simple event-driven serverless architecture using AWS services.

Whenever a file is uploaded to an Amazon S3 bucket, an AWS Lambda function is automatically triggered. The Lambda function then sends a notification using Amazon SNS, which delivers an email alert to the subscribed user.

---

## Architecture

S3 Bucket → Lambda Function → SNS Topic → Email Notification

---

## AWS Services Used

- Amazon S3
- AWS Lambda
- Amazon SNS
- Amazon CloudWatch
- AWS IAM

---

## Workflow

1. A file is uploaded to the S3 bucket.
2. The upload event triggers the Lambda function.
3. The Lambda function publishes a message to the SNS topic.
4. SNS sends an email notification to the subscribed email address.
5. CloudWatch logs are used to monitor Lambda execution.

---

## Features

- Event-driven architecture
- Automated notifications
- Serverless workflow
- CloudWatch monitoring
- AWS service integration

---

## Project Structure

```text
AWS-serverless-file-notification-system/
│
├── lambda-function/
├── screenshots/
├── architecture/
└── README.md
```

---

## Challenges Faced

- Configuring Lambda trigger permissions
- Understanding SNS subscription confirmation
- Connecting AWS services correctly
- Monitoring execution using CloudWatch logs

---

## Learning Outcomes

Through this project, I learned:

- Basics of serverless architecture
- AWS Lambda event triggers
- SNS notification workflows
- CloudWatch logging and monitoring
- AWS IAM permission handling

---

## Future Improvements

- Add SQS queue integration
- Add file type validation
- Store metadata in DynamoDB
- Create frontend upload interface

---

## Author

Bhoomi