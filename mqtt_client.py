import paho.mqtt.client as paho
from paho import mqtt

client = paho.Client()

client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set("vijay", "Elementure")
client.connect("61a171e69f90478f8cadd99e5d25f03b.s1.eu.hivemq.cloud",8883)


#data = [("topic","lock"),("12 pm","locked"),("6 am ", "unlocked")]

#for i in range(len(data)):
#client.publish("lock",payload=str(data[i]),qos=0)

#my_payload ='{"data":{"jid":118,"uid":"84:f7:3:67:79:b0","app":"door_gateway","evt":{"etm":"2022-03-167T11:17:21Z","dsd":4865}},"meta":{"ver":"1.0"}}'
#my_payload="{\"e90af4e6-b068-4ea6-a403-1ca4b87e9c04\":{\"data\":{\"jid\":23,\"devId\":\"2e0651ab-22cd-4170-9079-9f588f823296\",\"evt\":{\"etm\":\"2022-03-16T11:17:21Z\",\"csm\":20},\"dev\":\"water_measure\"},\"meta\":{\"ver\":\"1.0\",\"gId\":\"20e64e2d-27a2-4471-b0a4-97d0c426c3e4\"}},\"5b1a066a-06f0-4267-8a10-6fca1f18e242\":{\"data\":{\"jid\":24,\"devId\":\"2e0651ab-22cd-4170-9079-9f588f823296\",\"evt\":{\"etm\":\"2022-03-16T11:17:21Z\",\"csm\":20},\"dev\":\"water_measure\"},\"meta\":{\"ver\":\"1.0\",\"gId\":\"20e64e2d-27a2-4471-b0a4-97d0c426c3e4\"}},\"700ad45b-06a0-4345-8c1e-f534599b5935\":{\"data\":{\"jid\":25,\"devId\":\"2e0651ab-22cd-4170-9079-9f588f823296\",\"evt\":{\"etm\":\"2022-03-16T11:17:21Z\",\"csm\":20},\"dev\":\"water_measure\"},\"meta\":{\"ver\":\"1.0\",\"gId\":\"20e64e2d-27a2-4471-b0a4-97d0c426c3e4\"}},\"aeabc4d0-52e4-4448-8e89-5593eeb184df\":{\"data\":{\"jid\":26,\"devId\":\"2e0651ab-22cd-4170-9079-9f588f823296\",\"evt\":{\"etm\":\"2022-03-16T11:17:21Z\",\"csm\":20},\"dev\":\"water_measure\"},\"meta\":{\"ver\":\"1.0\",\"gId\":\"20e64e2d-27a2-4471-b0a4-97d0c426c3e4\"}},\"1bb38a9a-d49d-4b60-9900-4299b51b913e\":{\"data\":{\"jid\":27,\"devId\":\"2e0651ab-22cd-4170-9079-9f588f823296\",\"evt\":{\"etm\":\"2022-03-16T11:17:21Z\",\"csm\":20},\"dev\":\"water_measure\"},\"meta\":{\"ver\":\"1.0\",\"gId\":\"20e64e2d-27a2-4471-b0a4-97d0c426c3e4\"}}}"
my_payload = "{\"e90af4e6-b068-4ea6-a403-1ca4b87e9c04\":{\"data\":{\"jid\":23,\"devId\":\"2e0651ab-22cd-4170-9079-9f588f823296\",\"evt\":{\"etm\":\"2022-03-16T11:17:21Z\",\"csm\":20},\"dev\":\"water_measure\"},\"meta\":{\"ver\":\"1.0\",\"gId\":\"20e64e2d-27a2-4471-b0a4-97d0c426c3e4\"}"
# while True:
client.publish("lock",payload=my_payload,qos=1)
print("topic with name lock is published to a mqtt broker")


# client.disconnect()

client.loop_forever()
