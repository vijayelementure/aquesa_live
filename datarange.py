import boto3
import os

from dotenv import load_dotenv
import datetime

load_dotenv()

# dynamodb = boto3.client('dynamodb', region_name='us-east-1')
dynamodb = boto3.client('dynamodb',region_name = os.getenv('REGION_NAME'),aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
# Specify the table name and the primary key
table_name = 'aquesa_live'
partition_key = 'P_key'
# Specify the start and end dates for the date range
start_date = '2022-12-12'
end_date = '2022-12-12'
# Use the query() method to retrieve items within the date range
response = dynamodb.query(
    TableName=table_name,
    KeyConditionExpression=Key(partition_key).between(start_date, end_date)
)

print(response)
# Loop through the items in the response and print the date and other attributes
# for item in response['Items']:
#     date = item['date']['S']
#     other_attributes = item['other_attributes']['S']
#     print(f'Date: {date}, Other attributes: {other_attributes}')