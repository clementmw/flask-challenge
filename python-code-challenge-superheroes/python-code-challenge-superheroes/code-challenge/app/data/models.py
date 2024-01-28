from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heros'
    serialize_rules= ('-hero_powers.heros',)


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # relationship with HeroPower
    hero_powers = db.relationship('HeroPower', backref='hero', lazy='dynamic')

    def __repr__(self):
        return f"name: {self.name}"\
        f"super_name: {self.super_name}"\
        f"created_at: {self.created_at}"
        

class HeroPower(db.Model, SerializerMixin):
    __tablename__ = 'hero_powers'
    serialize_rules= ('-hero.hero_powers',)

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)
    # to establish connection to heroes
    hero_id = db.Column(db.Integer, db.ForeignKey('heros.id'))
    
    # to establish connection to power
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id',))

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f"strength: {self.strength}"\
        f"hero_id: {self.hero_id}"
        

class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'
    serialize_rules= ('-hero_powers.powers',)


    id = db.Column(db.Integer, primary_key = True)
    name  = db.Column(db.String)
    description  = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    # for relationship with HeroPower
    hero_powers = db.relationship('HeroPower', backref='power', lazy='dynamic')

    @validates('description')
    def  validate_description(self, key, description):   
        if  description is None and len(description) <20 :
            raise ValueError ("Description must be atleast 20 characters long")
        return  description  

    def __repr__(self):
        return f"name: {self.name}"\
        f"description: {self.description}"
