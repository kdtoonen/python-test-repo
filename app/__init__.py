from python_test_project import app
from model import db
app.static_folder = 'static'
db.init_app(app)
with app.app_context():
    # TODO: only do the database create when on dev. probably import some environment
    # TODO: variable and add a condition
    db.create_all()


