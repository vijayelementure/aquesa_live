import paho.mqtt.client as mqtt
import boto3
import os
import uuid
from dotenv import load_dotenv
import datetime
load_dotenv()
import json

dynamodb = boto3.resource('dynamodb',region_name = os.getenv('REGION_NAME'),aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
table = dynamodb.Table('aquesa_live')  

def message(pub,userdata,msg):
    #print(msg.topic)
    #print(msg.payload.decode('utf-8'))
    mypayload = json.loads(msg.payload.decode("utf-8"))
    for p_id, p_info in mypayload.items():
          print("\Device Data:",mypayload[p_id])   # for data
          
          devid = mypayload[p_id]['data']['devId']   # for partition key
          arrival_time = mypayload[p_id]['data']['evt']
          table.put_item(
            Item={"P_key": devid,
                  "S_key": str(datetime.datetime.now()),
                  "topic": msg.topic,
                  "payload" : mypayload[p_id]
              }
)

clientID = "acquesa-01"
broker = "a1nfm22n2z9lxw-ats.iot.ap-south-1.amazonaws.com"
port = 8883
pub = mqtt.Client(clientID)
pub.tls_set("./certificates/AmazonRootCA1.crt","./certificates/certificate.pem","./certificates/private.pem")
pub.connect(broker,port,45)
#pub.publish("/data", "i am from python", qos=1)

pub.subscribe("/data",qos=1)


pub.on_message = message
pub.loop_forever()





