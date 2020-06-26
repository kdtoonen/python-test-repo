from python_test_project import app
from model import db
import mysql.connector
# only run this if you want to create an empty databasecd
# TODO: remove hard coded shit from this file
# TODO: add condition for using local sqllite database for development purposes
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS " + app.config['DATABASE_NAME'])

db.init_app(app)
with app.app_context():
    print('dropping all tables')
    db.drop_all()
    print('creating all tables')
    db.create_all()




