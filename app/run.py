from python_test_project import app
from model import db
db.init_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

