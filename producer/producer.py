# from kafka import KafkaProducer
# import socket    
# import time    
# import json 
# import os
# from dotenv import load_dotenv
# from dotenv import dotenv_values
# from ensurepip import bootstrap

# load_dotenv()
# config = dotenv_values(".env")
# print(config)
# s = socket.socket() 
# HOST=os.getenv("HOST")
# PORT= int(os.getenv("PORT"))         
# s.connect(((HOST,int(PORT))))
# bootstrap_servers= os.getenv("bootstrap_servers")
# topic_name= os.getenv("topicname")
# topic_name=os.getenv("topic_name")
# bootstrap_servers=["scm-kafka-1:9092"]
# producer=KafkaProducer(bootstrap_servers=bootstrap_servers,value_serializer=lambda m: json.dumps(m).encode("utf-8"),
        #  retries=5)
# while True:
# 	try:
# 		data=s.recv(70240).decode()
# 		json_acceptable_string = data.replace("'", "\"")
# 		rec = json.loads(json_acceptable_string)
# 		for i in rec:
# 			producer.send(topic_name,i)
# 			print(i)
# 	except Exception as e:
# 		print(e)
# s.close() 
        







from ensurepip import bootstrap
import socket    
import json 
import os
from pathlib import Path
from dotenv import load_dotenv
from kafka import KafkaProducer

load_dotenv()

socket_connection = socket.socket()
# HOST = os.getenv("HOST")
# PORT = os.getenv("PORT")             
socket_connection.connect(("server",12345))
# bootstrap_servers =os.getenv("bootstrap_servers")  
bootstrap_servers ="kafka"

producer = KafkaProducer(bootstrap_servers = bootstrap_servers, retries = 5)

# topicName = os.getenv("topic_name")
topicName = "devicedatastream"
while True:
    try:
        data=socket_connection.recv(70240)
        # json_acceptable_string = data.replace("'", "\"")
        # load_data = json.loads(json_acceptable_string)
        # print(load_data)
        # for data in load_data:
        print(data)
        producer.send(topicName,data)

    except Exception as exception:
        print(exception)
socket_connection.close()

        








