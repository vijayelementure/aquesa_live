import boto3
import os
from dotenv import load_dotenv
import datetime

load_dotenv()


# Replace with your own DynamoDB table name, device ID, and date
table_name = "aquesa_live"
P_key = "3cebf247-4a2b-49b4-9c20-ade38c57b0da"
date = "2022-12-12"
            
# Create a boto3 client for DynamoDB
dynamodb = boto3.client('dynamodb',region_name = os.getenv('REGION_NAME'),aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
#table = dynamodb.Table('aquesa_live') 


# Use the query operation to retrieve data for the specified device ID and date
response = dynamodb.query(
    TableName=table_name,
    KeyConditionExpression="P_key = :did AND S_key BETWEEN :date_start AND :date_end",
    ExpressionAttributeValues={
        ":did": {"S": P_key},
        ":date_start": {"N": f"{date}T00:00:00"},
        ":date_end": {"N": f"{date}T23:59:59"},
    }
)

print(response)

# Initialize a variable to hold the sum of the consumption values
# consumption_sum = 0

# # Iterate over the data items in the response
# for item in response["Items"]:
#   # Check if the consumption attribute is a number
#   if "data" in item["consumption"]:
#     # Add the consumption value to the sum
#     consumption_sum += int(item["consumption"]["N"])

# # Print the sum of the consumption values
# print(consumption_sum)