import paho.mqtt.client as mqtt
import boto3
import os
import uuid
from dotenv import load_dotenv
import datetime
load_dotenv()
import json
import time 



dynamodb = boto3.resource('dynamodb',region_name = os.getenv('REGION_NAME'),aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
table = dynamodb.Table('aquesa_live')  

def message(pub,userdata,msg):
    print(msg.topic)
    # print(msg.payload)
    #print(msg.payload.decode('utf-8'))
    mypayload = json.loads(msg.payload.decode("utf-8"))
    
    for p_id, p_info in mypayload.items():
        #   print("\n")
          print("\Device Data:",mypayload[p_id])   # for data 
          devid = mypayload[p_id]['data']['devId']   # for partition key (devid is a partition key)
          arrival_time = mypayload[p_id]['data']['evt']['etm']
          print(arrival_time)

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
# pub.loop_start()
# time.sleep(20)
# pub.loop_stop()




