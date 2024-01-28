from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'Heros'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # relationship with HeroPower
    hero_powers = db.relationship('HeroPower', backref='hero')

    def __repr__(self):
        return f"name: {self.name}"\
        f"super_name: {self.super_name}"\
        

class HeroPower(db.Model):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)
    # to establish connection to heroes
    hero_id = db.Column(db.Integer, db.ForeignKey('Heros.id'))
    # to establish connection to power
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f"strength: {self.strength}"\
        f"hero_id: {self.hero_id}"\
        

class Power(db.model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key = True)
    name  = db.Column(db.String)
    description  = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    # for relationship with HeroPower
    hero_powers = db.relationship('HeroPower', backref='power')

    def __repr__(self):
        return f"name: {self.name}"\
        f"description: {self.description}"\
