# import paho.mqtt.client as paho
# from paho import mqtt
# import pymongo
# import json
# from datetime import datetime


# #myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

# myclient = pymongo.MongoClient("mongodb+srv://vijaybhaskar:vijay123@clusteracquesa.ycgsefc.mongodb.net/?retryWrites=true&w=majority")
# #db = myclient.test


# mydb = myclient["lock"]

# mycol = mydb["lock_status"]

# def message(client,userdata,msg):
#     print(msg.topic)
#     print(msg.payload)
#     # x = msg.payload
#     # data = json.loads(x)
    
#     # current_time = datetime.now()
    
#     # time_dict = {"Time":current_time}
    
#     # time_dict.update(data)
    
#     # mycol.insert_one(time_dict)

    
    
   
    
# #mycol.delete_many({})


# client = paho.Client(client_id="2", userdata=None, protocol=paho.MQTTv5)


# client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)

# client.username_pw_set("vijay", "Elementure")

# client.connect("61a171e69f90478f8cadd99e5d25f03b.s1.eu.hivemq.cloud",8883,60)

# client.subscribe("lock",qos=0)

# client.on_message = message

# print("subscribed to lock topic from client ",1)

# client.loop_forever()

# b'{"lock":"rajath"}'

