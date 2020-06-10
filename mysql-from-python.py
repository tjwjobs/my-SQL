import os
import pymysql

# Get username from gitpod workspace

username = os.getenv('GITPOD_USER')

# connect to database 

connection = pymysql.connect(host = 'localhost',
                            user = username,
                            password = '',
                            db = 'Chinook')

try:
    # run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall
        print(result)
finally:
    # close connection to sql, regardless of whether above is successful
    connection.close()
