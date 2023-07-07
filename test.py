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


# devid = ["137f03f4-0cd8-423b-804f-e2544dfe519b","54de714e-c3a2-4b53-b247-2bf4372f8a9c","2e35120e-3ba2-4323-9dec-1cf84ae9fcf0","a0624a52-1df2-4d26-bba8-0aa05c27d2b6"]
# for i in devid:
#     print(i)
#     print(type(i))

# while True:
#     print("aquesa")

# var = "XQK9mWMNfXM0JMFN9r76tnPcrbH3,2023-06-03 00:00:00.000"

# x = var.split(",")

# print(x)
# print("\n")
# print(x[0])
# print("\n")
# print(x[1])


# var = {'852359c0-07c9-4857-9b90-cc7dc2e9be1f': {'data': {'wtq': {'ph': 8.469, 'tds': 166.3, 'tmp': 24.66}, 'etm': '2023-6-15T14:41:08Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}
#        ,'37c4dc47-f84e-4861-90cc-1bab05c1fb93': {'data': {'wtq': {'ph': 8.467, 'tds': 163.6, 'tmp': 24.88}, 'etm': '2023-6-15T14:51:08Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        '02218ab4-9a7f-49bb-a1f3-04893391d5b3': {'data': {'wtq': {'ph': 8.467, 'tds': 163.1, 'tmp': 24.84}, 'etm': '2023-6-15T15:01:08Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        '3c2e6f18-9ea7-48b7-9b3e-417250842fb6': {'data': {'wtq': {'ph': 8.467, 'tds': 162.9, 'tmp': 24.83}, 'etm': '2023-6-15T15:11:08Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}},
#        'e6cc51b3-8569-4667-b19d-7fcb4e80c2cf': {'data': {'wtq': {'ph': 8.467, 'tds': 163.5, 'tmp': 24.95}, 'etm': '2023-6-15T15:21:08Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        'a587e055-3c38-4338-8212-5633d3b2d8fd': {'data': {'wtq': {'ph': 8.466, 'tds': 163.6, 'tmp': 25.02}, 'etm': '2023-6-15T15:31:08Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        'be6a5ca2-40c4-4281-8a2b-ea0bbdd645a6': {'data': {'wtq': {'ph': 8.466, 'tds': 164, 'tmp': 25.09}, 'etm': '2023-6-15T15:41:08Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        'e73011a9-912e-4791-ab62-ee2c1cdd29c7': {'data': {'wtq': {'ph': 8.465, 'tds': 163.8, 'tmp': 25.1}, 'etm': '2023-6-15T15:51:08Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        '3c0af640-b1ab-440e-813f-4d43775d3b2d': {'data': {'wtq': {'ph': 8.465, 'tds': 163.9, 'tmp': 25.18}, 'etm': '2023-6-15T16:01:08Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}},
#        'eb2fb3c6-9c77-47f9-80d3-883ec7fbd3f1': {'data': {'wtq': {'ph': 8.465, 'tds': 163.7, 'tmp': 25.12}, 'etm': '2023-6-15T16:11:08Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        '087ba306-8115-47c2-a3ab-ffc6fd8bfe75': {'data': {'wtq': {'ph': 8.464, 'tds': 163.1, 'tmp': 25.26}, 'etm': '2023-6-15T16:21:08Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        '2addd465-2e3d-4ce6-af63-3171723db18d': {'data': {'wtq': {'ph': 8.464, 'tds': 163.5, 'tmp': 25.3}, 'etm': '2023-6-15T16:31:08Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        '6e8fa4b6-dfd0-4b5d-b995-b4c0c32fcd0a': {'data': {'wtq': {'ph': 8.464, 'tds': 163.2, 'tmp': 25.35}, 'etm': '2023-6-15T16:41:08Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}},
#        'f436f2bc-4eab-4476-a5e5-14cef65a37f2': {'data': {'wtq': {'ph': 8.464, 'tds': 163.1, 'tmp': 25.4}, 'etm': '2023-6-15T16:51:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        '71b07980-3e97-487e-987a-b966c9897461': {'data': {'wtq': {'ph': 8.463, 'tds': 162.9, 'tmp': 25.42}, 'etm': '2023-6-15T17:01:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}},
#        'e3a0bc3d-2f41-4b2e-9723-1ed52768bea8': {'data': {'wtq': {'ph': 8.463, 'tds': 163.1, 'tmp': 25.47}, 'etm': '2023-6-15T17:11:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        '7878365c-4285-46f5-9c16-38c3431add99': {'data': {'wtq': {'ph': 8.463, 'tds': 163.1, 'tmp': 25.44}, 'etm': '2023-6-15T17:21:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        '020b12db-4c1b-4674-a763-7cb0988f0bd9': {'data': {'wtq': {'ph': 8.463, 'tds': 163, 'tmp': 25.46}, 'etm': '2023-6-15T17:31:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        '179b03f5-64b6-427a-9855-79a66bc0931d': {'data': {'wtq': {'ph': 8.462, 'tds': 162.8, 'tmp': 25.62}, 'etm': '2023-6-15T17:41:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        'd3c937d9-a3a8-42d7-b0af-a94165f97f8b': {'data': {'wtq': {'ph': 8.463, 'tds': 162.7, 'tmp': 25.54}, 'etm': '2023-6-15T17:51:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        'bba16e9b-913f-4360-b1fa-299f92ea3377': {'data': {'wtq': {'ph': 8.463, 'tds': 162.7, 'tmp': 25.58}, 'etm': '2023-6-15T18:01:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        'ceb4adf2-cc54-4b57-8f7b-a1e6013ec07c': {'data': {'wtq': {'ph': 8.463, 'tds': 162.6, 'tmp': 25.55}, 'etm': '2023-6-15T18:11:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        '4e0cc8e6-1d8f-4ca1-a048-ca1cb1cac5f9': {'data': {'wtq': {'ph': 8.463, 'tds': 162.5, 'tmp': 25.65}, 'etm': '2023-6-15T18:21:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        '81443c3f-de67-429e-b13b-3e662ad55edc': {'data': {'wtq': {'ph': 8.463, 'tds': 162.7, 'tmp': 25.64}, 'etm': '2023-6-15T18:31:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        'ff299702-0406-4be7-ad54-af4cd32699ed': {'data': {'wtq': {'ph': 8.463, 'tds': 162.3, 'tmp': 25.72}, 'etm': '2023-6-15T18:41:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        '93dcaa9e-24e8-4517-9e7b-c938d239492f': {'data': {'wtq': {'ph': 8.464, 'tds': 162.6, 'tmp': 25.63}, 'etm': '2023-6-15T18:51:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        'bdcdb79a-6532-4092-9a02-ee48dc8e72c8': {'data': {'wtq': {'ph': 8.464, 'tds': 162.4, 'tmp': 25.61}, 'etm': '2023-6-15T19:01:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        'b3f14144-1be5-44f5-9fb4-da41f547223e': {'data': {'wtq': {'ph': 8.464, 'tds': 162.3, 'tmp': 25.74}, 'etm': '2023-6-15T19:11:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        '29a8867d-b013-4a9d-bf6e-98696982e4e4': {'data': {'wtq': {'ph': 8.464, 'tds': 162.4, 'tmp': 25.71}, 'etm': '2023-6-15T19:21:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        'e414e92e-40a2-471a-8c6c-b0bf22100f52': {'data': {'wtq': {'ph': 8.464, 'tds': 162.3, 'tmp': 25.71}, 'etm': '2023-6-15T19:31:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        '15bddd93-8de5-4745-8009-ad4eb106b752': {'data': {'wtq': {'ph': 8.464, 'tds': 162.1, 'tmp': 25.76}, 'etm': '2023-6-15T19:41:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        '41eabbcb-954e-4758-be92-8c77185110c7': {'data': {'wtq': {'ph': 8.465, 'tds': 162.1, 'tmp': 25.75}, 'etm': '2023-6-15T19:51:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        '4e7272ec-677f-4d0a-975f-a7630eb7d9e5': {'data': {'wtq': {'ph': 8.465, 'tds': 162.3, 'tmp': 25.67}, 'etm': '2023-6-15T20:01:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        'c7a3654b-c607-41e5-9f39-c7d6fa6845ef': {'data': {'wtq': {'ph': 8.465, 'tds': 162.1, 'tmp': 25.72}, 'etm': '2023-6-15T20:11:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        '434284d4-618d-4848-96ae-9892d9fea6d7': {'data': {'wtq': {'ph': 8.466, 'tds': 162, 'tmp': 25.58}, 'etm': '2023-6-15T20:21:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}},
#        '0821d56c-3fae-4b4e-91c7-6ebcd9121123': {'data': {'wtq': {'ph': 8.466, 'tds': 161.9, 'tmp': 25.72}, 'etm': '2023-6-15T20:31:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}},
#        '4dc72f9e-da3c-4158-9833-cd37d0f89d2e': {'data': {'wtq': {'ph': 8.467, 'tds': 162, 'tmp': 25.68}, 'etm': '2023-6-15T20:41:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        'e8e73dea-f5fe-4ad7-89ff-432ae2f11d90': {'data': {'wtq': {'ph': 8.467, 'tds': 162.2, 'tmp': 25.64}, 'etm': '2023-6-15T20:51:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        '4821e746-da68-45c7-98dc-93de2d058a2b': {'data': {'wtq': {'ph': 8.467, 'tds': 162.1, 'tmp': 25.68}, 'etm': '2023-6-15T21:01:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}},
#        'dde16495-cb33-4ba8-b168-4b3680c0354a': {'data': {'wtq': {'ph': 8.468, 'tds': 162.1, 'tmp': 25.65}, 'etm': '2023-6-15T21:11:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        '5a2352ea-4345-44dd-93cf-b52527ddd636': {'data': {'wtq': {'ph': 8.469, 'tds': 162.1, 'tmp': 25.5}, 'etm': '2023-6-15T21:21:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        '6f1f321c-458e-476d-9e9b-aed31e7feb91': {'data': {'wtq': {'ph': 8.469, 'tds': 162.5, 'tmp': 25.59}, 'etm': '2023-6-15T21:31:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}},
#        'b4078199-0952-4adc-8a37-e46889d42f78': {'data': {'wtq': {'ph': 8.469, 'tds': 162.6, 'tmp': 25.67}, 'etm': '2023-6-15T21:41:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        '3b05674b-3ad1-495b-9893-14fe246fded4': {'data': {'wtq': {'ph': 8.469, 'tds': 162.2, 'tmp': 25.66}, 'etm': '2023-6-15T21:51:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        '368f787d-515f-4218-8664-54919d8da401': {'data': {'wtq': {'ph': 8.47, 'tds': 162, 'tmp': 25.58}, 'etm': '2023-6-15T22:01:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        'fdb2e20c-8b91-463d-bc48-5786eba4182f': {'data': {'wtq': {'ph': 8.471, 'tds': 162.1, 'tmp': 25.51}, 'etm': '2023-6-15T22:11:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        'b09db83b-fc15-40aa-b956-6aeb20bc551e': {'data': {'wtq': {'ph': 8.47, 'tds': 162.1, 'tmp': 25.52}, 'etm': '2023-6-15T22:21:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        '43573a39-d356-4e65-aaf1-9701468a3741': {'data': {'wtq': {'ph': 8.471, 'tds': 161.9, 'tmp': 25.47}, 'etm': '2023-6-15T22:31:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        'f81c9bc2-4551-4724-9d60-b91be4bd3802': {'data': {'wtq': {'ph': 8.472, 'tds': 161.7, 'tmp': 25.5}, 'etm': '2023-6-15T22:41:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}, 
#        '6da9251e-910e-489c-881f-3cc70376dfa1': {'data': {'wtq': {'ph': 8.472, 'tds': 161.7, 'tmp': 25.48}, 'etm': '2023-6-15T22:51:09Z'}, 'meta': {'ver': '1.0', 'gid': 'gateway', 'gId': 'orangepi'}}}



# print(var['852359c0-07c9-4857-9b90-cc7dc2e9be1f'])



var = {
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

import json

print(type(var))

print(type(json.dumps(var)))