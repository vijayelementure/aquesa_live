import boto3
from datetime import datetime
import os
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.requests import Request
import json
app = FastAPI()
from dotenv import load_dotenv
# from starlette.requests import Request

timenow = datetime.now()


class Item(BaseModel):
    user_id : str
    date_time : str


dynamodb = boto3.resource('dynamodb',region_name = os.getenv('REGION_NAME'),aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
table = dynamodb.Table('customer_account') 


@app.post('/csm')
async def consumption(request: Request):
    print("request data")
    rqst_info = await request.json()
    # print(type(rqst_info))
    print(rqst_info.get('customer_id'))
    
    resp_data = rqst_info.get('customer_id')
    
    split_data = resp_data.split(",")
    
    print("customer_id :",split_data[0])
    # print(split_data[1])
    
    # print(rqst_info.get('customer_id'))
    # print(rqst_info.get('data').get('customer_id'))
    response = table.query(
    # IndexName='customer_id-date_arraival-index',
    KeyConditionExpression="#pk = :pk",
    # FilterExpression="#devid = :devid",
    ProjectionExpression="consumption",
    ExpressionAttributeNames={"#pk": "customer_id"},
    ExpressionAttributeValues={
        # ":pk":"rqst_info.get('data').get('customer_id')"
        # ":pk": rqst_info.get('customer_id')
        # ":sk": "2e35120e-3ba2-4323-9dec-1cf84ae9fcf0"
        
        ":pk": split_data[0],
    },
)

    print("response data")
    print(response)
    
    total_csm = 0
    total_res = 0
    for item in response["Items"]:
        total_csm += item["consumption"]
        total_res = total_csm/10
    return total_res
    
# print("Total CSM:", total_csm/100)