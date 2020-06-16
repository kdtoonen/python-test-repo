from flask import Blueprint, render_template
from flask_login import login_required, current_user
import users
admin_page = Blueprint('admin_page', __name__, template_folder='templates')


@admin_page.route('/adminaccount')
@login_required
def render_admin_page():
    return render_template('adminpage.html')


