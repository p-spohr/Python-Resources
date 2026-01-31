# %%

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String

# %%

# os.getcwd()
basedir = os.path.abspath(os.path.dirname(__file__))


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


class Puppy(db.Model):
    # manually name table
    __tablename__ = 'puppies'
    
    id: Mapped[int] = mapped_column(primary_key= True)
    name: Mapped[str]
    age: Mapped[int]
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    # def __repr__(self):
    #     return f'{self.name} | {self.age}'