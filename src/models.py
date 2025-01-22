import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250))
    email = Column(String(250))
    password = Column(String(250))


    
class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    gender = Column(String(250))
    hair_color = Column(String(250))
    eye_color = Column(String(250))
    height = Column(String(250))
    birth_year = Column(String(250))

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    description = Column(String(250))
    diameter = Column(Integer)
    climate = Column(Integer)
    gravity = Column(Integer)
    terrain = Column(String(250))
    population = Column(Integer)

class Vehicle(Base):
    __tablename__ = 'vehicle' 
    id = Column(Integer, primary_key=True)
    model = Column(String(250))
    vehicle_class = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    character = relationship(Character)
    planet = relationship(Planet)
    vehicle = relationship(Vehicle)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
