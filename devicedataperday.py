import boto3
import os

from dotenv import load_dotenv
import datetime

load_dotenv()

dynamodb = boto3.client('dynamodb',region_name = os.getenv('REGION_NAME'),aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
table_name = 'aquesa_live'
partition_key = 'P_key'
start_date = "2022-12-13"
end_date = "2022-12-13"

response = dynamodb.query(
    TableName=table_name,
   KeyConditionExpression ="P_key=:P_key BETWEEN S_key=:S_key AND S_key=:S_key",
    ExpressionAttributeValues= {
        ":P_key": {
            "S": "baff91a7-2dbb-4461-82c7-5f48b1d227fe"
        },
        ":S_key": {
            "S": start_date
        },
         ":S_key": {
             "S": end_date
         }
    }
)

print(response['Items'])
# Loop through the items in the response and print the date and other attributes
# for item in response['Items']:
#     date = item['date']['S']
#     other_attributes = item['other_attributes']['S']
#     print(f'Date: {date}, Other attributes: {other_attributes}')