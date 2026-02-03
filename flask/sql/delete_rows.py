from database.orm import db, Puppy, app
import sqlalchemy
import sys


with app.app_context():
    
    try:
        pup = db.session.execute(db.select(Puppy).where(Puppy.name.ilike('snow'))).one()
    except:
        print('No puppy found with name Snow.')
        
    print(pup)
    print(pup[0])
    print(pup[0].id)
    
    
    
    del_stmt = db.delete(Puppy).where(Puppy.id == pup[0].id)
    print(del_stmt)
    
    db.session.execute(del_stmt)
    
    # sys.exit(1)
    
    # try:
    #     pup = db.session.execute(db.select(Puppy).where(Puppy.name.ilike('snow'))).one()
    #     print(pup[0])
    # except Exception as e:
    #     print(f'No puppy found with name Snow: {e}')
    
    
    db.session.commit()