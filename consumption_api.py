import boto3
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("TestProd")

app = FastAPI()



class deviceattr(BaseModel):
    deviceid: str
    startdate: str
    enddate: str



@app.post('/devID')
def Total_consumption(items:deviceattr):
    response = table.query(
        KeyConditionExpression="#pk = :pk and #sk between :start_date and :end_date",
    # FilterExpression="#devid = :devid",
        ProjectionExpression="consumption",
        ExpressionAttributeNames={"#pk": "device_id", "#sk": "data_time"},
        ExpressionAttributeValues={
        ":pk": items.deviceid,
        ":start_date": items.startdate,
        ":end_date": items.enddate,
    },
)
    total_csm = 0
    for item in response["Items"]:
        total_csm += item["consumption"]
    return total_csm/100




    
