from flask import Flask
from flask import render_template
# from flask.ext.pymongo import PyMongo
from flask_pymongo import PyMongo
from pymongo import MongoClient


# client = MongoClient('localhost:27017')
client = MongoClient("localhost", 27017)
db = client.zipcode
cities = db.code


app = Flask(__name__)
mongo = PyMongo(app)


# @app.route('/')
# def hello_world():
#     return 'Hello World ggg123!'

@app.route('/')
def bestCities():
    bestCities = []
    for city in cities.find().sort("pop"):
        bestCities.append(city)
    bestCities = bestCities[-20:]

    for city in bestCities:
        for key in city.keys():
            if key == 'pop':
                city['population'] = city[key]
                del city['pop']

    print '>>>>>>>>>>>>>>', bestCities
    # cities = mongo.db.test.find().sort({"pop": -1})
    return render_template('index.html', cities=bestCities)

if __name__ == '__main__':
    app.run()
