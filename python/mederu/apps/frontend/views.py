from flask import Blueprint
from flask import session, redirect, url_for, request, render_template

frontend = Blueprint('frontend', __name__, url_prefix='/frontend', template_folder='templates', static_folder='static')

@frontend.route('/')
def frontend_index():
    if 'username' in session:
        return render_template('frontend/index.html')
    return 'You are not logged in'

@frontend.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@frontend.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
