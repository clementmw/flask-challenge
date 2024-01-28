#!/usr/bin/env python3

from flask import Flask, make_response,request,jsonify
from flask_migrate import Migrate
from flask_restful import Resource, Api
from werkzeug.exceptions import NotFound

from models import db, Hero,HeroPower,Power

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

migrate = Migrate(app, db)

db.init_app(app)

@app.errorhandler(NotFound)
def handle_not_found(e):
    response= make_response("NotFound: The requested resource not found", 404)
    return response


@app.route('/')
def home():
    response = make_response('welcome to superhero')
    return response

class Heroes(Resource):
    def get(self):
        response_dict =[record.to_dict() for record in  Hero.query.all()]
        return jsonify(response_dict)

       
api.add_resource(Heroes, '/heroes')

class HeroesByID(Resource):
    def get(self, id):
        record = Hero.query.get(id)

        if not record:
            error = {"error": "Hero not found"}
            response = make_response(jsonify(error), 404)
        else:
            response = make_response(jsonify(record.to_dict()), 200)

        return response

api.add_resource(HeroesByID, '/heroes/<int:id>')

# class Power(Resource):
#      def get(self):
#         get_power = Power.query.all()
#         power_dict = [record.to_dict() for record in get_power]
#         response = make_response(jsonify(power_dict), 200)
#         return response
        
        
api.add_resource(Power, '/powers')



if __name__ == '__main__':
    app.run(port=5555, debug = True)
