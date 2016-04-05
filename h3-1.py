
import pymongo

connection = pymongo.MongoClient('mongodb://localhost')
db = connection.school
students = db.students

for student in students.find():

    scores = student['scores']
    lowestHWScore = None

    # print(scores)

    for index, score in enumerate(scores):

        if score['type'] == 'homework':

            if lowestHWScore is None or scores[index]['score'] < scores[lowestHWScore]['score']:
                lowestHWScore = index

    scores.pop(lowestHWScore)

    student['scores'] = scores
    students.save(student)
    print('Saved: ' + str(student['_id']))

    # print(scores)
    # print('======================')



