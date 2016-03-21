import pymongo
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)

db = connection.test

names = db.names

names.insert_one({'name': 'Dan Ossorio'})

item = names.find_one()

print(item['name'])
