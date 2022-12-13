import paho.mqtt.client as paho
from paho import mqtt
import pymongo
import json
import datetime
import pytz
import tzlocal
import boto3

dynamodb = boto3.resource('dynamodb',region_name = "ap-south-1",aws_access_key_id="AKIATZHKUJIM7W4P3EMJ",aws_secret_access_key="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")
table = dynamodb.Table('aquesaDB')  

#myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")


# myclient = pymongo.MongoClient("mongodb+srv://vijaybhaskar:vijay123@clusteracquesa.ycgsefc.mongodb.net/?retryWrites=true&w=majority")
# db = myclient.test



# mydb = myclient["lock1"]

# mycol = mydb["lock_status1"]

a = "vijay"


def message(client,userdata,msg):
    # print(msg.topic)
    # print(msg.payload)
    # print(type(msg.payload.decode()))
    payloadDATA = (msg.payload.decode()).split()
    #print(payloadDATA)
    print(payloadDATA[0])
    
    ht = table.put_item(
    Item={"part_key":"aquesadata",
          "sort_key": str(datetime.datetime.now()),
          "topic": msg.topic,
          "payload" :msg.payload.decode(),
        }
)
    # x = msg.payload
    # data = json.loads(x)
    
    # utc_time = datetime.datetime.utcnow()
    
    # time_dict = {"time": utc_time}
    
    # time_dict.update(data)
     
    # mycol.insert_one(time_dict)

    
    
   
    
#mycol.delete_many({})


client = paho.Client(client_id="2", userdata=None, protocol=paho.MQTTv5)


client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)

client.username_pw_set("vijay", "Elementure")

client.connect("61a171e69f90478f8cadd99e5d25f03b.s1.eu.hivemq.cloud",8883,60)

client.subscribe("lock",qos=1)

client.on_message = message

#print("subscribed to lock topic from client ",1)

client.loop_forever()
