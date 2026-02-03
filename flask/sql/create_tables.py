from database.orm import db, Puppy, app
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import MetaData
import sqlalchemy
import pathlib, sys

metadata_obj = MetaData()
    
user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement= True),
    Column("name", String(30)),
    Column("fullname", String),
)
print(user_table)
print(user_table.c)
print(user_table.c.keys())
print(user_table.c.name)
print(user_table.metadata.tables.keys())

db_name = 'database/test.db'
db_path = pathlib.Path(__file__).absolute().parent.joinpath(db_name)

db_api = db_path.as_uri().replace('file', 'sqlite', 1)

print(db_api)

engine = sqlalchemy.create_engine(db_api, echo= True)

user_table.create(engine, checkfirst= True)
# user_table.create(engine, checkfirst= False) # always check if table exists using checkfirst

with app.app_context():
    # Puppy and db both have same metadata
    # print(Puppy.metadata.tables.keys())
    print(db.metadata.tables.keys())
    
    # creates tables based on current metadata (separate from test.db, config in app)
    db.create_all()

    
