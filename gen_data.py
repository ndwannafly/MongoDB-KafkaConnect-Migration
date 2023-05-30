from pymongo import MongoClient
import random
from faker import Faker
client = MongoClient('mongodb://mongo-source:27017/')

db = client['test']
collection = db['users']
fake = Faker()

for i in range(10000):
    # Generate the data for the document
    data = {
        'name': fake.name(),
        'email': fake.email(),
        'age': random.randint(20, 60),
    }
    # Insert the document into the collection
    collection.insert_one(data)

print("Data inserted successfully!")
