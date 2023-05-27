import boto3
import os
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

dynamodb = boto3.resource('dynamodb',region_name = os.getenv('REGION_NAME'),aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
table = dynamodb.Table('TestProd') 


class deviceattr(BaseModel):
    deviceid: str
    startdate: str
    enddate: str

@app.post('/jsoncount')
def json_count(items:deviceattr):
     response = table.query(
        KeyConditionExpression="#pk = :pk and #sk between :start_date and :end_date",
        ProjectionExpression="json_id",
        ExpressionAttributeNames={"#pk": "device_id", "#sk": "device_time"},
        ExpressionAttributeValues={
        ":pk": items.deviceid,
        ":start_date": items.startdate,
        ":end_date": items.enddate,
    }
)
     
     #print(response["Items"])
     jsoncount = response["Items"]
     print(len(jsoncount))
     return jsoncount
