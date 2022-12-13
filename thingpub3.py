import paho.mqtt.client as mqtt


clientID = "acquesa"
broker = "a1nfm22n2z9lxw-ats.iot.ap-south-1.amazonaws.com"
port = 8883
pub = mqtt.Client(clientID)
pub.tls_set("./certificates/AmazonRootCA1.crt","./certificates/certificate.pem","./certificates/private.pem")
pub.connect(broker,port,45)
while True:
    pub.publish("/data", "i am from kotlin", qos=1)

pub.loop_forever()
