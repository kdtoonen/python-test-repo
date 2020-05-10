from flask import Flask, current_app, g
import sqlite3
app = Flask(__name__)
app.config.from_object('appconfig')
DATABASE = app.config['DATABASE']


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


def get_db():
    db = getattr(g, '_database', None)

    if db is None:

        db = g._database = sqlite3.connect(DATABASE, isolation_level=None)
    db.row_factory = sqlite3.Row
    return db

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
