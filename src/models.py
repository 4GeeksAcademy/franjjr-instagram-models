import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False, unique=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(50))
    password = Column(String(16), nullable=False)
    
class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    description = Column(String(500))
    img_url = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    users = relationship('Users')

    def to_dict(self):
        return {}

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)   
    name = Column(String, nullable=False) 

class Characters_Films(Base):
    __tablename__ = 'characters_films'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.id'))
    character = relationship('Characters', foreign_keys=['character_id'])
    film_id = Column(Integer, ForeignKey('films.id'))
    film = relationship('Films', foreign_keys=['film_id'])
    minutes = Column(DateTime)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    homeworld_Id = Column(Integer, ForeignKey('planets.id'))
    homeworld = relationship('Planets')


class Films(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    year = Column(DateTime)
    director = Column(String(50))



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
