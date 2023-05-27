import json
import time
import datetime

import boto3
import logging

# Setting Logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Setting DynamoDB
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("TestProd")


def datetimetounix(dttime):
    d1 = datetime.datetime.strptime(dttime, "%Y-%m-%dT%H:%M:%SZ")
    d1tounix = int(time.mktime(d1.timetuple()))
    return d1tounix


def insertdatatoddb(data):
    try:
        table.put_item(Item=data)
    except Exception as e:
        logger.error("Error: %s" % e)


def get_arrival_time():
    d = datetime.datetime.utcnow()
    return int(d.timestamp())
    

def get_string_formatted_time():
    dt = datetime.datetime.utcnow()
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def lambda_handler(event, context):
    # Extract the message data from the AWS IoT event
    # print(event) # As it's RAW Data
    trialdata = json.dumps(event)
    # print(trialdata) # Raw Data
    # print(type(trialdata))
    createdata = json.loads(trialdata)
    for p_id, p_info in createdata.items():
        print(createdata[p_id])  # Json Payload from Node
        print(createdata[p_id]["data"]["evt"]["etm"])  # Time
        intime = datetimetounix(createdata[p_id]["data"]["evt"]["etm"])
        print(intime)
        data = {}
        data["device_id"] = createdata[p_id]["data"]["devId"]
        data["data_time"] = get_string_formatted_time()
        data["device_time"] = createdata[p_id]["data"]["evt"]["etm"]
        data["data_timestamp"] = get_arrival_time()
        data["device_timestamp"] = intime
        data["json_id"] = createdata[p_id]["data"]["jid"]
        data["consumption"] = createdata[p_id]["data"]["evt"]["csm"]
        data["battery_voltage"] = createdata[p_id]["data"]["binf"]["bvt"]
        data["battery_powered_on"] = createdata[p_id]["data"]["binf"]["bpon"]
        data["device_type"] = createdata[p_id]["data"]["dev"]
        data["version"] = createdata[p_id]["meta"]["ver"]
        data["gateway_id"] = createdata[p_id]["meta"]["gId"]
        insertdatatoddb(data)

    # message = json.loads(event)

    # Print the message data to the Lambda function's log stream
    # print(f"Message: {json.dumps(message)}")
