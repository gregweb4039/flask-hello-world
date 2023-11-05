from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect('postgres://lab10_db_pvd9_user:Ye7i4QvXGpsZkSQbZ6Es7wFZpGUfHWyC@dpg-cl3rea1novjs73bnl7n0-a/lab10_db_pvd9')
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def creating():
    conn = psycopg2.connect('postgres://lab10_db_pvd9_user:Ye7i4QvXGpsZkSQbZ6Es7wFZpGUfHWyC@dpg-cl3rea1novjs73bnl7n0-a/lab10_db_pvd9')
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"