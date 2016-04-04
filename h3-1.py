
import pymongo

connection = pymongo.MongoClient('mongodb://localhost')
db = connection.school
students = db.students

for student in students.find():
    scores = student["scores"]
    for index, score in enumerate(scores):
        if ()
        print(index, score)

        break
    break

