from models import db, app, Puppy, Owner, Toy


# puppy_names = [
#     'Brownie',
#     'Snow',
#     'Rainbow',
#     'Bandit',
#     'Floppy'
# ]

puppy_names = [
    'Hammy',
]

def query_print(table):
    table_name = table.__tablename__
    results = table.query.all()
    if len(results) > 0:
        print(f'{table_name} has {len(results)} items.')
        for row in results:
            print(row)
    else:
        print(f'{table_name} has no results.')
    print('-' * 50)

with app.app_context():
    query_print(Puppy)
    query_print(Owner)
    query_print(Toy)
        
    
        
        