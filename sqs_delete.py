import boto3
import dotenv
import os
from dotenv import load_dotenv

load_dotenv()

resource = boto3.client("sqs",region_name=os.getenv('REGION_NAME'),aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))

service_url = "https://sqs.ap-south-1.amazonaws.com/260337584665/WaterMeter.fifo"

response = resource.receive_message(
    QueueUrl=service_url,
    AttributeNames=["SentTimestamp"],
    MaxNumberOfMessages=1,
    MessageAttributeNames=["All"],

)

print("response......\n")
print(response)

Reciept_handler = response["Messages"][0]["ReceiptHandle"]

print("Reciept_handler......\n")
print(Reciept_handler)

resource.delete_message(
     QueueUrl= service_url,
     ReceiptHandle=str(Reciept_handler)
 )