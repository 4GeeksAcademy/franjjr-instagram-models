import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_from = relationship('User', foreign_keys=['user.id'])
    user_to_id = Column(Integer, ForeignKey('user.id'))
    user_to = relationship('User', foreign_keys=['user.id'])

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False, unique=True)
    firstname = Column(String(40), nullable=False)
    lastname = Column(String(40))
    email = Column(String(50), nullable=False, unique=True)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_post_id = Column(Integer, ForeignKey('user.id'))
    user_post = relationship('User', foreign_keys=['user.id'])
    
class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum, nullable=False)
    url = Column(String)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('Post')

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(200), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'))
    author = relationship('User', foreign_keys=['user.id'])  
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('Post', foreign_keys=['post.id'])


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
