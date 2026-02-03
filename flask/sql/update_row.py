from database.orm import db, Puppy, app
import sqlalchemy
import sys


with app.app_context():
    
    # 1. OPTION - GRAB OBJECT, CHANGE, ADD BACK
    pup = db.session.execute(db.select(Puppy).where(Puppy.name.ilike('snow'))).one()
    
    print(pup)
    print(pup[0])
    
    pup[0].age = 10
    print(pup[0])
    
    db.session.add(pup[0])
    
    # 2. OPTION - USE update()
    stmt = db.update(Puppy).where(
        sqlalchemy.and_(
            Puppy.name == 'Snow',
            Puppy.id == pup[0].id
        )
    ).values(name= 'SNOW')
    
    print(stmt)
    
    # sys.exit(1)
    
    db.session.execute(stmt)
    
    pup = db.session.execute(db.select(Puppy).where(Puppy.name.ilike('snow'))).one()
    
    print(pup)
    print(pup[0])
    
    db.session.commit()
 
