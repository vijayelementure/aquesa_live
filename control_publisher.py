import paho.mqtt.client as mqtt
import time 
import json

clientID = "acquesa"
broker = "a1nfm22n2z9lxw-ats.iot.ap-south-1.amazonaws.com"
port = 8883
pub = mqtt.Client(clientID)
pub.tls_set("./certificates/AmazonRootCA1.crt","./certificates/certificate.pem","./certificates/private.pem")
pub.connect(broker,port,45)

ondata = {"data":{"devId":"3d498f89-581f-4d38-bcf1-86aca516f51c","app":"waterMeter","ctrl":1},"meta":{"ver":"1.0"}}
offdata = {"data":{"devId":"3d498f89-581f-4d38-bcf1-86aca516f51c","app":"waterMeter","ctrl":0},"meta":{"ver":"1.0"}}

pub.loop_start()
while True:
    pub.publish("/switchcontrol",json.dumps(ondata), qos=1)
    time.sleep(15)
    pub.publish("/switchcontrol", json.dumps(offdata), qos=1)
    time.sleep(15)

pub.loop_forever()
    

