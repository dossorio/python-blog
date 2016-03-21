import bottle
import pymongo

@bottle.route('/')
def index():

    connection = pymongo.MongoClient('localhost', 27017)
    db = connection.test
    name = db.names
    name = name.find_one()

    return bottle.template('index', {'user': name['name'], 'things': ['one', 'two', 'three']})

@bottle.post('/favourite-number')
def favourite_number():
    number = bottle.request.forms.get('number')

    if number is None or number == '':
        number = 'No number selected!'

    bottle.response.set_cookie('number', number)
    return bottle.redirect('/show-number')

@bottle.route('/show-number')
def show_number():
    number = bottle.request.get_cookie('number')
    return bottle.template('favourite_number', {'number': number})



bottle.debug(True)
bottle.run(host='localhost', port=8080)
