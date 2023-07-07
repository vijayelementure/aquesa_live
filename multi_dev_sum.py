import boto3
from datetime import datetime
import os
from fastapi import FastAPI

app = FastAPI()

timenow = datetime.now()


dynamodb = boto3.resource('dynamodb',region_name = os.getenv('REGION_NAME'),aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
table = dynamodb.Table('TestProd') 

  # Change DevID
# start_timestamp = int(
#     datetime(2023, 5, 18, 00, 00, 00).timestamp()
# )  # Change start time with Date If Required
# end_timestamp = int(
#     datetime(2023, 5, 18, 23, 59, 59).timestamp()
# )  # Change end time with Date If Required

# start_timestamp = str(datetime(2023, 5, 17, 00, 00, 00)) # Change start time with Date If Required
# end_timestamp = str(datetime(2023, 5, 18, 23, 59, 59)) # Change end time with Date If Required



devid = ["bbff3163-00d5-4cdc-927e-b25170e13f48","54de714e-c3a2-4b53-b247-2bf4372f8a9c","2e35120e-3ba2-4323-9dec-1cf84ae9fcf0","a0624a52-1df2-4d26-bba8-0aa05c27d2b6","78ad7e34-3b2c-4232-9781-0a131de9e93e"]

#2023-05-19 15:59:10.417072
start_timestamp = "2023-06-11T00:00:00Z"
end_timestamp = "2023-06-12T23:59:59Z"


print(end_timestamp)

@app.post('/csm')
def consumption():
    total_csm = 0
    for i in devid:
        response = table.query(
    KeyConditionExpression="#pk = :pk and #sk between :start_date and :end_date",
    # FilterExpression="#devid = :devid",
    ProjectionExpression="consumption",
    ExpressionAttributeNames={"#pk": "device_id", "#sk": "data_time"},
    ExpressionAttributeValues={
        ":pk": i,
        ":start_date": start_timestamp,
        ":end_date": end_timestamp,
    },
)

    

    
        for item in response["Items"]:
            total_csm += item["consumption"]
        total_res = total_csm/10
    return total_res
    
    
# print("Total CSM:", total_csm/100)