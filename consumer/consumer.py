# import pymongo
# import json
# import time
# import sys
# import os
# from kafka import KafkaConsumer
# from pymongo import MongoClient
# from dotenv import load_dotenv
# from dotenv import dotenv_values

# load_dotenv()
# from config.db import MONGO_URI

# bootstrap_servers= os.getenv("bootstrap_servers")
# topic_name= os.getenv("topicname")
# client = pymongo.MongoClient(os.getenv("MONGO_URI"))
# config = dotenv_values(".env")
# connection=MongoClient(config["MONGO_URI"])

# DB_NAME=Scmxpert
# mydb=connection['Scmxpert1']
# mycollection=mydb.get_collection("Device_data")
# topic_name="Device_data"
#bootstrap_servers=["scm-kafka-1:9092"]
# Consumer=KafkaConsumer(topic_name,bootstrap_servers=bootstrap_servers,auto_offset_reset="earliest")
# try:
#     for rec in Consumer:        
#         rec=json.loads(rec.value)       
#         n=mycollection.insert_one(rec)
#         print(n)
# except Exception as  e:
#     print(e)







import socket   
import os 
import time    
import pymongo   
import json 
import sys
from kafka import KafkaConsumer
from dotenv import load_dotenv
load_dotenv()


# CLIENT = pymongo.MongoClient(os.getenv("MONGO_URI"))
CLIENT = pymongo.MongoClient("mongodb+srv://subbareddy:subbareddy123@cluster0.yjrvgmv.mongodb.net/test")
DB = CLIENT['Scmxpert1']
DATA_STREAM = DB["Device_data"]

# topicName = os.getenv("topic_name")    
topicName = "devicedatastream"
print(topicName)
# bootstrap_servers= os.getenv("bootstrap_servers")
bootstrap_servers= "kafka"
consumer = KafkaConsumer(
    topicName,
    bootstrap_servers = bootstrap_servers,
    auto_offset_reset = 'latest',
    group_id ='group-A')
try:
    # consumer = KafkaConsumer(topicName,bootstrap_servers = bootstrap_servers,auto_offset_reset = 'earliest')
    for d in consumer:
        try:
            d = json.loads(d.value)
            print(d)
            mdata = DATA_STREAM.insert_one(d)
        except json.decoder.JSONDecodeError:
            continue
except KeyboardInterrupt:
    sys.exit()

