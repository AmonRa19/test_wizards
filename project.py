# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from flask_pymongo import PyMongo
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.zipcode
cities = db.code

app = Flask(__name__)
mongo = PyMongo(app)


@app.route('/')
def sort_cities():

    most_p_cities = [city for city in cities.find().sort("pop")][-20:]
    for city in most_p_cities:
        for key in city.keys():
            if key == 'pop':
                city['population'] = city[key]
                del city['pop']

    return render_template('index.html', cities=most_p_cities)


if __name__ == '__main__':
    app.run()
