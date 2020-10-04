import os
import sqlite3
from flask import Flask, g

DATABASE = './banco.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


app = Flask(__name__)
app.secret_key = 'lms-impacta'


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if not os.path.exists(DATABASE):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()

    with open('banco.sql') as s:
        sql = s.read()
        conn.executescript(sql)
        conn.commit()

    conn.close()


from controllers import *


if __name__ == "__main__":
    app.run(debug=True)
