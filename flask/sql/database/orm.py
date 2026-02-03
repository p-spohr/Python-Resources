# %%

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String

# %%

# os.getcwd()
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


db.init_app(app)


class Owner(db.Model):
    # manually name table
    # __tablename__ = 'owners'
    
    id: Mapped[int] = mapped_column(primary_key= True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    age: Mapped[int]
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def __repr__(self):
        return f'{self.id:<5} | {self.first_name:<15} | {self.last_name:<15} | {self.age:<5}'
    
class Puppy(db.Model):
    # manually name table
    # __tablename__ = 'puppies'
    
    id: Mapped[int] = mapped_column(primary_key= True)
    name: Mapped[str]
    age: Mapped[int]
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f'{self.id:<5} | {self.name:<15} | {self.age:<5}'
    
class Home(db.Model):
    # manually name table
    # __tablename__ = 'homes'
    
    id: Mapped[int] = mapped_column(primary_key= True)
    city: Mapped[str]
    state: Mapped[int]
    
    def __init__(self, city, state):
        self.city = city
        self.state = state
        
    def __repr__(self):
        return f'{self.id:<5} | {self.city:<15} | {self.state:<15}'