import sqlite3
from flask import g
from app import app

DATABASE = '../db/aosc2018.db'

@app.route('/')
@app.route('/index')
def index():
    return ('Know your home')

@app.route('/api/allusers')
def allusers():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute('''SELECT * FROM "UserTable";''')
    result=str(cur.fetchall())
    cur.connection.close()
    return (result)
