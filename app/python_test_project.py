from flask import Flask, render_template, request, redirect
from flask_login import LoginManager, login_required, login_user, logout_user, UserMixin, current_user
import users
from admin_page import admin_page


app = Flask(__name__)
app.config.from_object('appconfig')
app.debug = True
app.register_blueprint(admin_page)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@app.route('/',  methods=['GET'])
def index():
    return render_template('landing.html', messageStatus="", loginStatus="")


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


@app.route('/createaccount', methods=('GET', 'POST'))
def create_account():
    if request.method == 'GET':
        return render_template('landing.html', messageStatus="", loginStatus="")
    elif request.method == 'POST':
        username = request.form.get('e_mail')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        if users.this_user_exists_already(username):
            return render_template('landing.html', messageStatus="You already have an account, "
                                                                 "would you like to reset it and receive "
                                                                 "a change password link?", loginStatus="")
        else:
            success = users.create_user(username, first_name, last_name)
            if success:
                return render_template('landing.html', messageStatus="Your account has been created, "
                                                                 "please check you e-mail for "
                                                                 "further instructions", loginStatus="")
            else:
                return render_template('landing.html', messageStatus="Something went wrong creating your "
                                                                 "account, please contact the site  "
                                                                 "administrator", loginStatus="")


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

    #TODO: FIX THIS
    def set_userInfo(self, userinfo):
        self.userInfo = userinfo
        self.name = self.userInfo[0]


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)



