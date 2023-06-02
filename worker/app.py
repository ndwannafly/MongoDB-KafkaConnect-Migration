from kafka import KafkaConsumer
import pymongo
from json import loads

mongo_client = pymongo.MongoClient('mongodb://mongo-target:27017')
mongo_collection = mongo_client['test']['users']

topic = 'test.users'
bootstrap_servers = 'kafka:9092'
consumer = KafkaConsumer(
    topic, bootstrap_servers=bootstrap_servers, auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda x: loads(x.decode('utf-8'))
    )

for msg in consumer:
    print(msg.value)
    try:
        mongo_collection.insert_one(msg.value)
    except Exception as e:
        print(f"Error writing message {e}")
