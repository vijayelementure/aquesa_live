import paho.mqtt.client as mqtt
import boto3
import os
import uuid
from dotenv import load_dotenv
import time
load_dotenv()

dynamodb = boto3.resource('dynamodb',region_name = "ap-south-1",aws_access_key_id="AKIATZHKUJIM7W4P3EMJ",aws_secret_access_key="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")
table = dynamodb.Table('acquesa_data')  

def message(pub,userdata,msg):
    print(msg.topic)
    print(msg.payload)
    ht = table.put_item(
    Item={"deviceid":"FA2022V01MDRN00000005",
          "topic": msg.topic,
          "payload" : str(msg.payload)
        }
)

clientID = "acquesa-01"
broker = "a1nfm22n2z9lxw-ats.iot.ap-south-1.amazonaws.com"
port = 8883
pub = mqtt.Client(clientID)
pub.tls_set("./certificates/AmazonRootCA1.crt","./certificates/certificate.pem","./certificates/private.pem")
pub.connect(broker,port,45)
pub.publish("/data", "i am from python", qos=1)

pub.subscribe("/data",qos=1)

pub.on_message = message
pub.loop_forever()

print()






