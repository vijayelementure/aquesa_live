import boto3
import os

from dotenv import load_dotenv
import datetime

load_dotenv()

# dynamodb = boto3.client('dynamodb', region_name='us-east-1')
dynamodb = boto3.client('dynamodb',region_name = os.getenv('REGION_NAME'),aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
resp = dynamodb.execute_statement(Statement='SELECT * FROM aquesa_live WHERE "P_key" = "baff91a7-2dbb-4461-82c7-5f48b1d227fe" AND "S_key" >= "2022-12-13 12:31:18.191122" AND "S_key" <= "2022-12-13 12:43:18.488046"')
print(resp)
# sum = 0
# for item in resp['Items']:
#     print(item['P_key'])
#     # print(item)
#     # print(item['payload']['M']['data']['M']['evt']['M']['csm']['N'])
#     print(item['payload']['M']['data']['M']['evt']['M']['csm']['N'])
#     sum += int(item['payload']['M']['data']['M']['evt']['M']['csm']['N'])
#     # print(datetime.datetime.fromtimestamp(int(item['P_timestamp'])).strftime('%Y-%m-%d %H:%M:%S'))

# print("water consumption = %d" % (sum/10))



# {{query1.data.Items['0'].payload.data.evt.csm
# }}