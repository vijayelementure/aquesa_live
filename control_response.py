import paho.mqtt.client as mqtt
import uuid
import datetime


def message(pub,userdata,msg):
    print(msg.topic)
    print(msg.payload.decode('utf-8'))
    # print(type(msg.payload.decode('utf-8')))
    
    
    
clientID = "acquesa-01"
broker = "a1nfm22n2z9lxw-ats.iot.ap-south-1.amazonaws.com"
port = 8883
pub = mqtt.Client(clientID)
pub.tls_set("./certificates/AmazonRootCA1.crt","./certificates/certificate.pem","./certificates/private.pem")
pub.connect(broker,port,45)
#pub.publish("/data", "i am from python", qos=1)

pub.subscribe("/respdata",qos=1)


pub.on_message = message
pub.loop_forever()

print()






