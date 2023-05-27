import boto3
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("TestProd")

devid = "19dd1b26-9c42-49d1-b67f-5b2d17f1e9bc"  # Change DevID
start_timestamp = int(
    datetime(2023, 5, 18, 00, 00, 00).timestamp()
)  # Change start time with Date If Required
end_timestamp = int(
    datetime(2023, 5, 18, 23, 59, 59).timestamp()
)  # Change end time with Date If Required

print(end_timestamp)

def consumption(deviceid,start_time,end_time):
        response = table.query(
        KeyConditionExpression="#pk = :pk and #sk between :start_date and :end_date",
    # FilterExpression="#devid = :devid",
        ProjectionExpression="consumption",
        ExpressionAttributeNames={"#pk": "device_id", "#sk": "data_time"},
        ExpressionAttributeValues={
        ":pk": devid,
        ":start_date": start_time,
        ":end_date": end_time,
    },
)
    
    
total_csm = 0
for item in response["Items"]:
    total_csm += item["consumption"]

print("Total CSM:", total_csm)



consumption(devid,start_timestamp,end_timestamp)