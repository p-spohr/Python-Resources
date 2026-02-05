import os, pathlib
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from sqlalchemy import Integer, String, ForeignKey
from typing import List

from dotenv import load_dotenv


db_name = 'app.db'
base_dir = pathlib.Path(__file__).absolute().parent 
app_dir = base_dir.joinpath(db_name).as_uri().replace('file', 'sqlite')

# FLASK_APP=models.py
load_dotenv(base_dir.joinpath('.env'))

app = Flask(__name__)
app.secret_key = 'password'
app.config['SQLALCHEMY_DATABASE_URI'] = app_dir
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(app, model_class= Base)
Migrate(app, db) # already calls db.init_app(app)


# https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#declarative-table-with-mapped-column
class Puppy(db.Model):
    # primary keys must be Python int
    id: Mapped[int] = mapped_column(primary_key= True, autoincrement= True)
    name: Mapped[String] = mapped_column(String(50))
    # one-to-many relationship: the puppy has many toys; back_populates corresponds with 'puppy' reference in Toy
    # lazy="dynamic" only applies to collections (one‑to‑many).
    toys: Mapped[List['Toy']] = relationship(back_populates= 'puppy', lazy= 'dynamic')
    # one-to-one: one puppy has own owner
    owner: Mapped['Owner'] = relationship(back_populates= 'puppy', uselist= False)
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        if self.owner:
            get_toys = [toy for toy in db.session.execute(self.toys).scalars()]
            return f"Puppy name is {self.name}, owner is {self.owner.name}, and has toys: {get_toys}."
        else:
            return f"Puppy name is {self.name} and has no owner yet!"
    def report_toys(self):
        print("Here are my toys:")
        for toy in self.toys:
            print(toy.item_name)


class Toy(db.Model):
    id: Mapped[int] = mapped_column(primary_key= True, autoincrement= True)
    item_name: Mapped[String] = mapped_column(String(50))
    # Foreign key
    puppy_id: Mapped[Integer] = mapped_column(ForeignKey('puppy.id'))
    # many-to-one relationship: the toy belongs to one puppy
    # back_populates corresponds with 'toys' reference/relationship in Puppy
    puppy: Mapped['Puppy'] = relationship(back_populates= 'toys')
    def __init__(self, item_name, puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id
    def __repr__(self):
        return f"{self.item_name} belongs to {self.puppy.name}"

class Owner(db.Model):
    id: Mapped[int] = mapped_column(primary_key= True, autoincrement= True)
    name: Mapped[String] = mapped_column(String(50))
    puppy_id: Mapped[Integer] = mapped_column(ForeignKey('puppy.id'))
    # one-to-one: each owner has one puppy
    puppy: Mapped['Puppy'] = relationship(back_populates= 'owner')
    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id
    def __repr__(self):
        # get_puppy = db.session.execute(self.puppy_id)
        return f"{self.name} has the puppy called {self.puppy.name}."