# # import paho.mqtt.client as paho
# # from paho import mqtt
# # import pymongo
# # import json
# # from datetime import datetime


# # #myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

# # myclient = pymongo.MongoClient("mongodb+srv://vijaybhaskar:vijay123@clusteracquesa.ycgsefc.mongodb.net/?retryWrites=true&w=majority")
# # #db = myclient.test


# # mydb = myclient["lock"]

# # mycol = mydb["lock_status"]

# # def message(client,userdata,msg):
# #     print(msg.topic)
# #     print(msg.payload)
# #     # x = msg.payload
# #     # data = json.loads(x)
    
# #     # current_time = datetime.now()
    
# #     # time_dict = {"Time":current_time}
    
# #     # time_dict.update(data)
    
# #     # mycol.insert_one(time_dict)

    
    
   
    
# # #mycol.delete_many({})


# # client = paho.Client(client_id="2", userdata=None, protocol=paho.MQTTv5)


# # client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)

# # client.username_pw_set("vijay", "Elementure")

# # client.connect("61a171e69f90478f8cadd99e5d25f03b.s1.eu.hivemq.cloud",8883,60)

# # client.subscribe("lock",qos=0)

# # client.on_message = message

# # print("subscribed to lock topic from client ",1)

# # client.loop_forever()

# # b'{"lock":"rajath"}'


# # def consumption(x,y,z):
# #     a=x
# #     b=y
# #     c=z
# #     print(a)
# #     print(b)
# #     print(c)


# # a="1"
# # b="2"
# # c="3"
# # consumption(a,b,c)



# cnodes = [
#         {
#             "nodeid": "84e1a8f9-0122-48e6-8f6b-6f66f5a34b23",
#             "gatewayid": "d95af6d6-10fd-4706-bafc-26129114cfc9",
#             "projectid": "AQS2305A001",
#             "loci_d": "AQS2305A001",
#             "loc_name": "engrace",
#             "p_source": "On Battery",},
#         {
#             "nodeid": "84e1a8f9-0122-48e6-8f6b-6f66f5a34b23",
#             "gatewayid": "d95af6d6-10fd-4706-bafc-26129114cfc9",
#             "projectid": "AQS2305A001",
#             "loci_d": "AQS2305A001",
#             "loc_name": "engrace",
#             "p_source": "On Battery",
#         },
#     ]

# data =[]
# for item in cnodes:
#     x =0
    
    
# print(item.items[0])

# list2 = [1,2,3,4,5,6,7,8]
# list1 = [1,2,3,4,5]

# del list1
# print(list2)


# import datetime
# d1 = datetime.datetime.strptime("2013-07-12T07:00:00Z","%Y-%m-%d"+"T"+"%H:%M:%S"+"Z")

# print(d1)

# import requests

# response = requests.get("https://ap-south-1.console.aws.amazon.com/dynamodbv2/home?region=ap-south-1#item-explorer?table=TestProd&maximize=true")
# print(response.raw)


devid = ["137f03f4-0cd8-423b-804f-e2544dfe519b","54de714e-c3a2-4b53-b247-2bf4372f8a9c","2e35120e-3ba2-4323-9dec-1cf84ae9fcf0","a0624a52-1df2-4d26-bba8-0aa05c27d2b6"]
for i in devid:
    print(i)
    print(type(i))