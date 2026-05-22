import json
import boto3

sns = boto3.client('sns')

TOPIC_ARN = 'arn:aws:sns:eu-north-1:951865903432:file-upload-alerts'

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