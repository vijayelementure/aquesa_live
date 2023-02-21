import boto3
import os

from dotenv import load_dotenv
import datetime

load_dotenv()

device_list = ['22ad83a2-75de-4238-be92-67ed773be318','3cebf247-4a2b-49b4-9c20-ade38c57b0da','24ec8e23-371f-47df-9444-75e07b71b0e2']

# dynamodb = boto3.client('dynamodb', region_name='us-east-1')
dynamodb = boto3.client('dynamodb',region_name = os.getenv('REGION_NAME'),aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
for i in device_list:
    resp = dynamodb.execute_statement(Statement='SELECT * FROM aquesa_live WHERE P_key = ?', Parameters =[{'S':i}])
# print(resp['Items'])
    sum = 0
    for item in resp['Items']:
        print(item['P_key'])
        device_id = str(item['P_key'])
        dev_id = item['P_key']['S']
        #print(type(dev_id))
    # print(item)
    # print(item['payload']['M']['data']['M']['evt']['M']['csm']['N'])
        print(item['payload']['M']['data']['M']['evt']['M']['csm']['N'])
        sum += int(item['payload']['M']['data']['M']['evt']['M']['csm']['N'])
    # print(datetime.datetime.fromtimestamp(int(item['P_timestamp'])).strftime('%Y-%m-%d %H:%M:%S'))

    print("water consumption of DeviceId = " + (dev_id)+" is %d" %(sum/10))
    print("\n")


# {{query1.data.Items['0'].payload.data.evt.csm
# }}