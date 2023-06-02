import os
import faust
import pymongo

app = faust.App('app')

@app.on_configured.connect
def configure(app, conf, **kwargs):
    conf.broker = 'kafka://broker:9092;broker:29092'

mongo_client = pymongo.MongoClient('mongodb://mongo-target:27017')
mongo_collection = mongo_client['test']['users']

class MyRecord(faust.Record):
    name: str
    age: int
    email: str

    @property
    def sex(self):
        return "male"

@app.agent(topic='test.users')
async def even_records(records):
    async for record in records.filter(lambda r: r.even):
        my_record = MyRecord(name=record.name, age=record.age, even=record.email)
        my_record.sex = my_record.sex  # add a new field
        mongo_collection.insert(my_record.asdict())  # insert to MongoDB

if __name__ == '__main__':
    app.main()
