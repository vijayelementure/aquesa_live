import boto3 
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.requests import Request

app = FastAPI()

load_dotenv()

dynamodb = boto3.resource('dynamodb',region_name = os.getenv('REGION_NAME'),aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
table = dynamodb.Table('customer_details') 

@app.post('/ids')
async def create_customer_ids(request : Request):
    rqst_info = await request.json()
    print(rqst_info.get('data').get('customer_id'))
    print(rqst_info.get('data').get('device_id'))
    response = table.put_item(
    Item={
        "CustomerIDs": rqst_info.get('data').get('customer_id'),
        "DeviceIDs": rqst_info.get('data').get('device_id'),
    })
    
    return response