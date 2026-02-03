import sys
from dotenv import dotenv_values
import os
import mysql.connector

# mysql-connector-python is the library with the connector for mysql

# import mariadb
# import pymysql

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
DB_CONFIG = dotenv_values(path)

# Connect to platform
try:
    conn = mysql.connector.connect(
        user= DB_CONFIG['DB_USER'],
        password= DB_CONFIG['DB_PASS'],
        host= DB_CONFIG['DB_HOST'],
        port= 3307, # SSH tunnel from 3307:localhost:3306
        database= DB_CONFIG['DB_NAME']
    )
except ConnectionError as e:
    print(f'Error connecting to MySQL Platform: {e}')
    sys.exit(1)

conn.autocommit = False

# Get Cursor
cur = conn.cursor()
cur.execute('SELECT * FROM test_table')

for row in cur:
    print(f'{row[0]:<15} | {row[1]:<5}')
    
cur.close()
conn.close()