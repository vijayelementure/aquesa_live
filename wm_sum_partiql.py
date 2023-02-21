import boto3
import os

from dotenv import load_dotenv
import datetime

load_dotenv()

# dynamodb = boto3.client('dynamodb', region_name='us-east-1')
dynamodb = boto3.client('dynamodb',region_name = os.getenv('REGION_NAME'),aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
resp = dynamodb.execute_statement(Statement='SELECT * FROM aquesa_live WHERE P_key = ?', Parameters =[{'S': 'e687f849-41ba-4ec0-9f95-10988a081458'}])
# print(resp['Items'])
sum = 0
for item in resp['Items']:
    print(item['P_key'])
    # print(item)
    # print(item['payload']['M']['data']['M']['evt']['M']['csm']['N'])
    print(item['payload']['M']['data']['M']['evt']['M']['csm']['N'])
    sum += int(item['payload']['M']['data']['M']['evt']['M']['csm']['N'])
    # print(datetime.datetime.fromtimestamp(int(item['P_timestamp'])).strftime('%Y-%m-%d %H:%M:%S'))

print("water consumption = %d" % (sum/10))



# {{query1.data.Items['0'].payload.data.evt.csm
# }}