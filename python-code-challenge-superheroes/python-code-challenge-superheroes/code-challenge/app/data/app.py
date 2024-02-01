#!/usr/bin/env python3

from flask import Flask, make_response, request, jsonify
from flask_migrate import Migrate
from flask_restful import Api,Resource
from werkzeug.exceptions import NotFound
# from sqlalchemy.ext.declarative import declarative_base

from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# base = declarative_base()


migrate = Migrate(app, db)

db.init_app(app)

api= Api(app)

@app.errorhandler(NotFound)
def handle_not_found(e):
    response= make_response("NotFound: The requested resource not found", 404)
    return response

@app.route('/')
def home():
    return "Week 1 code challenge"

class Heroes(Resource):
    def get(self):
       get_hero = Hero.query.all()
       hero_dict = [hero.serialize()for hero in get_hero]
       response= make_response(jsonify(hero_dict), 200)
       return response


api.add_resource(Heroes, '/heroes')

class HeroesByID(Resource):
    def get(self,id):
        record=  Hero.query.get(id)
        
        if not record:
            error_dict=  {"error": "Hero not found"}
            response= make_response(jsonify(error_dict), 404 )
            return response
        else:
            record_dict= record.serialize()
            response= make_response(jsonify(record_dict), 200)
            return response
        
api.add_resource(HeroesByID, '/heroes/<int:id>')

class Powers(Resource):
    def get(self):
        get_power = Power.query.all()
        power_dict = [power.serialize() for power in get_power]
        response = make_response(jsonify(power_dict), 200)
        return response
     

api.add_resource(Powers, '/powers')

class PowersByID(Resource):
    def get(self,id):
        record=  Power.query.get(id)
        if not record:
            error_dict=  {"error": "Power not found"}
            response= make_response(jsonify(error_dict), 404)
            return response
        else:
            record_dict= record.serialize()
            response= make_response(jsonify(record_dict), 200)
            return response
    
    def patch(self,id):
        data = request.get_json()
        name = data.get("name")
        description = data.get("description")

        existing_id = Power.query.get(id)
        if not existing_id:
            return {"error":"id does not exist"}
        else:
            existing_id.name = name
            existing_id.description = description

            db.session.commit()

            response = make_response(jsonify(existing_id.serialize()),200)
            return response             

api.add_resource(PowersByID, '/powers/<int:id>')

class HeroPowers(Resource):
    def post(self):
        data = request.get_json()
        strength = data.get("strength")
        hero_id = data.get("hero_id")
        power_id = data.get("power_id")

        new_record = HeroPower(strength=strength, hero_id=hero_id, power_id=power_id)

        db.session.add(new_record)
        db.session.commit()

        response = make_response(jsonify(new_record.serialize()), 200)
        return response


    

       
    
api.add_resource(HeroPowers, '/heropowers')   
     
if __name__ == '__main__':
    app.run(port=5555, debug=True)
