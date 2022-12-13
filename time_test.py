import paho.mqtt.client as mqtt
import boto3
import os
import uuid
from dotenv import load_dotenv
import time
load_dotenv()

dynamodb = boto3.resource('dynamodb',region_name = os.getenv('REGION_NAME'),aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
table = dynamodb.Table('acquesa_data')  

def message(pub,userdata,msg):
    print(msg.topic)
    print(msg.payload) 
    table.put_item(
      Item={"deviceid":"FA2022V01MDRN00000005",
          "topic": msg.topic,
          "payload" : msg.payload.decode("utf-8")
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

print()






