from flask import Blueprint, render_template
from flask_login import login_required, current_user
import users
admin_page = Blueprint('admin_page', __name__, template_folder='templates')

@admin_page.route('/adminaccount')
@login_required
def render_admin_page():
    return render_template('adminbughunt.html')


@admin_page.route.route('/delete/<int:id>')
@login_required
def delete(id):
    user_to_delete = users.query.get_or_404(id)

    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting your account'

@admin_page.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    user = Users.query.get_or_404(id)

    if request.method == 'POST':
        user.name = request.form['name']
        user.email = request.form['email']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating user'

    else:
        return render_template('update.html', user=user)