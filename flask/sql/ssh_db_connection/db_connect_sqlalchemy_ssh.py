import sys, os
import urllib.parse
from dotenv import dotenv_values
import sqlalchemy

# <sql_dialect+python_lib>://<dbuser>:<dbpass>@<hostname:port>/<dbname>
# Use sqlalchemy.URL.create() to simplify URL creation and automatically escape password

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')

DBCON = dotenv_values(path)

# 1. OPTION - MANUAL
# password needs to be escaped
PASS = urllib.parse.quote_plus(DBCON['DB_PASS'])
DIALECT = f'{DBCON['DB_DIALECT']}+{DBCON['DB_PY']}'
HPORT = 3307 # SSH tunnel from 3307:localhost:3306

DB_URL = f'{DIALECT}://{DBCON['DB_USER']}:{PASS}@{DBCON['DB_HOST']}:{HPORT}/{DBCON['DB_NAME']}'

# 2. OPTION - URL OBJECT
url_object = sqlalchemy.URL.create(
    DIALECT,
    username= DBCON['DB_USER'],
    password= DBCON['DB_PASS'],  # plain (unescaped) text
    host= DBCON['DB_HOST'],
    database= DBCON['DB_NAME'],
    port = HPORT
)

print(DB_URL)
print(url_object)

engine = sqlalchemy.create_engine(url_object, echo= True)

try:
    with engine.connect() as conn:
        result = conn.execute(sqlalchemy.text('SELECT * FROM test_table'))
        for row in result:
            print(f'{row.name:<15} | {row.age:<5}')
except ConnectionError as e:
    print(f'Error connecting to MySQL Platform: {e}')
    sys.exit(1)
