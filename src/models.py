from flask_sqlalchemy import SQLAlchemy
from utils import get_current_date


db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(20))
    creation_date = db.Column(db.String(10), default=get_current_date)

    favorite = db.relationship('Favorite', back_populates='user')

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "username": self.username,
            "email": self.email,
            "creation_date": self.creation_date
        }


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    gender = db.Column(db.String(20))
    birth_date = db.Column(db.String(10))
    height = db.Column(db.Integer)
    hair_color = db.Column(db.String(50))
    eye_color = db.Column(db.String(50))
    skin_color = db.Column(db.String(50))
    url_image = db.Column(db.String(200), unique=True, )
    description = db.Column(db.String(200))

    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    planet = db.relationship('Planet', back_populates='character')

    """ favorite = db.relationship('Favorite', back_populates='character') """
    vehicle = db.relationship('Vehicle', back_populates='character')
    starship = db.relationship('Starship', back_populates='character')

    def __repr__(self):
        return '<Character %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "birth_date": self.birth_date,
            "height": self.height,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "skin_color": self.skin_color,
            "url_image": self.url_image,
            "description": self.description,
            "planet_id": self.planet_id
        }


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    population = db.Column(db.Integer)
    terrain = db.Column(db.String(50))
    climate = db.Column(db.String(50))
    orbit_period = db.Column(db.Integer)
    orbit_rotation = db.Column(db.Integer)
    diameter = db.Column(db.Integer)
    url_image = db.Column(db.String(200), unique=True)
    description = db.Column(db.String(200))

    """ favorite = db.relationship('Favorite', back_populates='planet') """
    character = db.relationship('Character', back_populates='planet')

    def __repr__(self):
        return '<Planet %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "terrain": self.terrain,
            "climate": self.climate,
            "orbit_period": self.orbit_period,
            "orbit_rotation": self.orbit_rotation,
            "diameter": self.diameter,
            "url_image": self.url_image,
            "description": self.description,
        }


class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    model = db.Column(db.String(100))
    vehicle_class = db.Column(db.String(100))
    passengers = db.Column(db.Integer)
    max_speed = db.Column(db.Integer)
    consumables = db.Column(db.Integer)
    url_image = db.Column(db.String(200), unique=True)
    description = db.Column(db.String(200))

    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    character = db.relationship('Character', back_populates='vehicle')

    """ favorite = db.relationship('Favorite', back_populates='vehicle') """

    def __repr__(self):
        return '<Vehicle %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "vehicle_class": self.vehicle_class,
            "passengers": self.passengers,
            "max_speed": self.max_speed,
            "consumables": self.consumables,
            "url_image": self.url_image,
            "description": self.description,
            "character_id": self.character_id
        }


class Starship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    model = db.Column(db.Integer)
    manufacturer = db.Column(db.String(120))
    length = db.Column(db.Integer)
    crew = db.Column(db.Integer)
    passengers = db.Column(db.Integer)
    cargo_capacity = db.Column(db.Integer)
    created = db.Column(db.String(70))
    consumables = db.Column(db.Integer)

    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    character = db.relationship('Character', back_populates='starship')

    """ favorite = db.relationship('Favorite', back_populates='starship') """

    def __repr__(self):
        return '<Starship %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers,
            "cargo_capacity": self.cargo_capacity,
            "created": self.created,
            "consumables": self.consumables,
            "character_id": self.character_id
        }


class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='favorite')

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', back_populates='favorite')

    # The FK of character, planet, vehicle, etc.
    category_fk_id = db.Column(db.Integer)

    def __repr__(self):
        return 'Favorite %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "category_id": self.category_id,
            "category_fk_id": self.category_fk_id
        }


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(30))

    favorite = db.relationship('Favorite', back_populates='category')

    def __repr__(self):
        return 'Category %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "category_name": self.category_name
        }
