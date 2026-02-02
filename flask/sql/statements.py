from database.orm import db, Puppy, app
import sqlalchemy
import sqlalchemy.sql.ddl as ddl
import sqlalchemy.sql.dml as dml

    
with app.app_context():
    print(sqlalchemy.select(Puppy))
    print(sqlalchemy.delete(Puppy))
    print(sqlalchemy.insert(Puppy))

    print(ddl.CreateTable(Puppy))
    print(ddl.DropTable(Puppy))

    print(dml.Update(Puppy))
    print(dml.Delete(Puppy))
    print(dml.Insert(Puppy))
    