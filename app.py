import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Patrick Ridley in 3308'

@app.route('/db_test')
def testing():
    conn = psycopg2.conn("postgresql://flask_hello_world_lab10_db_user:kD8xdq4ABY0dsj2mZPqvhY3jCSolD8HH@dpg-cvhmiaqqgecs73d28a00-a/flask_hello_world_lab10_db")
    conn.close()
    return 'Database connection successful - pari8094'
