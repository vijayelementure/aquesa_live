import paho.mqtt.client as mqtt


clientID = "acquesa"
broker = "a1nfm22n2z9lxw-ats.iot.ap-south-1.amazonaws.com"
port = 8883
pub = mqtt.Client(clientID)
pub.tls_set("./certificates/AmazonRootCA1.crt","./certificates/certificate.pem","./certificates/private.pem")
pub.connect(broker,port,45)

jdata = {'data': {'jid': 14, 'devId': '8233b4c5-9f03-4038-bd24-78751032d569', 'evt': {'etm': '2023-04-03T07:32:25Z', 'csm': 0}, 'bv': 3501, 'dev': 'water_measure'}, 'meta': {'ver': '1.0', 'gId': 'orangepi'}}

pub.publish("/data", "i am from python", qos=1)

pub.loop_forever()
