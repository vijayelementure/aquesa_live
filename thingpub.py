import paho.mqtt.client as mqtt
import json

clientID = "acquesa"
broker = "a1nfm22n2z9lxw-ats.iot.ap-south-1.amazonaws.com"
port = 8883
pub = mqtt.Client(clientID)
pub.tls_set("./certificates/AmazonRootCA1.crt","./certificates/certificate.pem","./certificates/private.pem")
pub.connect(broker,port,45)

jdata = {
  "4650c9e7-8d3f-4196-9c2d-26dd8c977023": {
    "data": {
      "jid": 2,
      "devId": "54de714e-c3a2-4b53-b247-2bf4372f8a9c",
      "evt": {
        "etm": "2023-07-07T11:05:14Z",
        "csm": 3
      },
      "binf": {
        "bvt": 400,
        "bpon": True
      },
      "dev": "water_measure"
    },
    "meta": {
      "ver": "1.0",
      "gId": "7c21c5c1-6c1d-46ec-82b6-e9b532087051"
    }
  }
}

var_data = json.dumps(jdata)

pub.publish("/data", var_data, qos=1)

pub.loop_forever()
