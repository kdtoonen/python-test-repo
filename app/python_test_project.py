from flask import Flask, render_template, request, redirect
from flask_login import LoginManager, login_required, login_user, logout_user, UserMixin, current_user
import users
from admin_page import admin_page

from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object('appconfig')
app.debug = True
app.register_blueprint(admin_page)
login_manager = LoginManager()


@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'GET':
        return render_template('landing.html', messageStatus="", loginStatus="")
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if users.password_and_username_ok(username, password):
            user_id = users.get_user_id()
            user = User(user_id)
            login_user(user)

            return render_template('main.html')
        else:
            return render_template('landing.html', messageStatus="", loginStatus="login failed")


@app.route('/',  methods=['GET'])
def index():
    return render_template('landing.html', messageStatus="", loginStatus="")



class User:

    def __init__(self, user_id):
        self.userid = user_id
        self.name = None
        self.userInfo = None

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.userid

    #DIT FIXEN
    def set_userInfo(self, userinfo):
        self.userInfo = userinfo
        self.name = self.userInfo[0]


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)



