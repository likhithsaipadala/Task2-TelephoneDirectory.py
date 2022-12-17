import pymongo
import pandas as pd
import json
client= pymongo.MongoClient("mongodb://localhost:27017")
df = pd.read_csv("TelephoneDirectory.csv")
data=df.to_dict(orient="record")
print(data)
db = client["CRUD_operations"]
print(db)
db.TelephoneDirectory.insert_many(data)

