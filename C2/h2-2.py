
import pymongo
from bson.objectid import ObjectId

connection = pymongo.MongoClient('mongodb://localhost')
db = connection.students
grades = db.grades

homework_grades = grades.find({'type': 'homework'}).sort([('student_id', pymongo.DESCENDING), ('score', pymongo.DESCENDING)])


def delete():
    counter = 1
    for grade in homework_grades:
        if counter % 2 == 0:
            grades.delete_one({'_id': ObjectId(grade['_id'])})
        counter += 1

    print('done')

