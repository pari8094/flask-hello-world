import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Patrick Ridley in 3308'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://flask_hello_world_lab10_db_user:kD8xdq4ABY0dsj2mZPqvhY3jCSolD8HH@dpg-cvhmiaqqgecs73d28a00-a/flask_hello_world_lab10_db")
    conn.close()
    return 'Database Connection Successful'

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgresql://flask_hello_world_lab10_db_user:kD8xdq4ABY0dsj2mZPqvhY3jCSolD8HH@dpg-cvhmiaqqgecs73d28a00-a/flask_hello_world_lab10_db")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball (
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
    ''')
    conn.commit()
    conn.close()
    return 'Basketball table Successfully Created'

@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect("postgresql://flask_hello_world_lab10_db_user:kD8xdq4ABY0dsj2mZPqvhY3jCSolD8HH@dpg-cvhmiaqqgecs73d28a00-a/flask_hello_world_lab10_db")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return 'Basketball Table Populated'

@app.route('/db_select')
def selecting():
    conn = psycopg2.connect("postgresql://flask_hello_world_lab10_db_user:kD8xdq4ABY0dsj2mZPqvhY3jCSolD8HH@dpg-cvhmiaqqgecs73d28a00-a/flask_hello_world_lab10_db")
    cur = conn.cursor()
    cur.execute('''
        Select * FROM Basketball;
    ''')
    records = cur.fetchall()
    conn.close()
    response_string=""
    response_string+="<table>"
    for player in records:
        response_string+="<tr>"
        for info in player:
            response_string+="<td>{}</td>".format(info)
        resonse_string+="</tr>"
    response_string+="</tables>"
    return response_string

@app.route('/db_drop')
def dropping():
    conn = psycopg2.connect("postgresql://flask_hello_world_lab10_db_user:kD8xdq4ABY0dsj2mZPqvhY3jCSolD8HH@dpg-cvhmiaqqgecs73d28a00-a/flask_hello_world_lab10_db")
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE Basketball;;
    ''')
    conn.commit()
    conn.close()
    return 'Basketball Table Dropped'
