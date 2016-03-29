
import json
from urllib import request
import pymongo

connection = pymongo.MongoClient('mongodb://localhost')
db = connection.reddit
stories = db.stories

# stories.drop()
# req = request.Request('http://www.reddit.com/r/technology/.json')
# req.add_header('User-agent', 'Mozilla/5.0')
# reddit_page = request.urlopen(req)
#
# parsed_reddit = json.loads(reddit_page.read().decode())
#
# print('Adding reddit posts')
# for item in parsed_reddit['data']['children']:
#     stories.insert_one(item['data'])
#
# print('Finished adding reddit posts')


def find():
    print('Keyword search started')

    query = {'title': {'$regex': 'apple|google', '$options': 'i'}}
    projection = {'title': 1, '_id': 0}

    try:
        cursor = stories.find(query, projection)
    except Exception as e:
        print('Unexpected error', type(e), e)

    for post in cursor:
        print(post)

find()
