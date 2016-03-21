import bottle
import pymongo

@bottle.route('/')
def index():

    connection = pymongo.MongoClient('localhost', 27017)
    db = connection.test
    name = db.names
    name = name.find_one()

    return bottle.template('index', {'user': name['name'], 'things': ['one', 'two', 'three']})

bottle.debug(True)
bottle.run(host='localhost', port=8080)
