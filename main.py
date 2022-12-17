from pymongo import MongoClient
from pymongo.errors import CollectionInvalid
from collections import OrderedDict

db = MongoClient("mongodb://localhost:27017/")['CRUD_operations']

user_schema = {
    'first_name': {
        'type' : 'string',
        'required' : True,
    },
    'last_name' : {
        'type' : 'string',
        'required' : True,
    },
    'city' : {
        'type' : 'string',
        'required' : True,
    },
    'country' : {
        'type' : 'string',
        'required' : True,
    },
    'state' : {
        'type' : 'string',
        'required' : True,
    },
    'zip' : {
        'type' : 'string',
        'required' : True,
    },
    'phone1' : {
        'type' : 'string',
        'required' : True,
    },
    'phone' : {
        'type' : 'string',
        'required' : True,
    }
}


collection = 'CRUD'
validator = {'$jsonSchema': {'bsonType':'object'}}
required=[]

if len(required) > 0:
    validator['$jsonSchema']['required'] = required

query = [('collMod', collection),
         ('validator', validator)]

db.create_collection(collection)

command_result = db.command(OrderedDict(query))