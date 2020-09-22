from flask import Flask, render_template, request, redirect
from flask_login import LoginManager, login_required, login_user, logout_user, UserMixin, current_user
from admin_page import admin_page
import messages, users, reservation

from services import services

app = Flask(__name__)
app.config.from_object('appconfig')
app.register_blueprint(services)
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
            user_id = users.get_user_id(username)
            user = User(user_id)
            login_user(user)
            user_data = users.get_user_info(user_id)
            reservations = reservation.get_reservations_for_user(user_id)

            return render_template('main.html', userData=user_data, listOfReservations=reservations)
        else:
            return render_template('landing.html', messageStatus="", loginStatus="login failed")


@app.route('/logoff', methods=('GET', 'POST'))
def logoff():
    logout_user()
    return render_template('landing.html', messageStatus="Logged off", loginStatus="Not logged in")


@app.route('/createaccount', methods=('GET', 'POST'))
def create_account():
    if request.method == 'GET':
        return render_template('landing.html', messageStatus="", loginStatus="")
    elif request.method == 'POST':
        username = request.form.get('e_mail')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        empty_value_check = users.check_new_user_first_last_and_user_name(username, first_name, last_name)
        if empty_value_check:
            return render_template('landing.html', messageStatus=empty_value_check, loginStatus="")
        elif users.this_user_exists_already(username):
            return render_template('landing.html', messageStatus=messages.message_account_was_already_created,
                                   loginStatus="")
        else:
            user_create_successful = users.create_user(username, first_name, last_name)
            if user_create_successful:
                return render_template('landing.html', messageStatus=messages.message_account_is_created,
                                       loginStatus="")
            else:
                return render_template('landing.html', messageStatus=messages.message_error_creating_account,
                                       loginStatus="")


@app.route('/resetpassword', methods=('GET', 'POST'))
def reset_password():
    if request.method == 'GET':
        email = request.args.get('email')
        reset_code = request.args.get('reset_code')
        return render_template('resetpassword.html', reset_code=reset_code, email_address=email)
    elif request.method == 'POST':
        password = request.form.get('password')
        password_again = request.form.get('password_again')
        email = request.form.get('email')
        reset_code = request.form.get('reset_code')
        if users.password_follows_rules(password, password_again):
            if users.reset_user_password(email, password, reset_code):
                return render_template('main.html', userData=({"firstname": "test", "lastname": "testtest"}))
            else:
                return render_template('resetpassword.html', reset_code=reset_code,
                                       email_address=email, message=messages.message_cannot_set_password)
        else:
            return render_template('resetpassword.html', reset_code=reset_code,
                                   email_address=email, message=messages.message_cannot_set_password)


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

