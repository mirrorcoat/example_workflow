from functools import wraps
from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = b'\xd4\x84\xb8\x1dU\xbc]l\xf6\xe2r\xf2q\x95M\x01'

from user import routes

def login_required(f):
    @wraps(f)
    def wrap(*arg, **kwargs):
        if 'logged_in' in session:
            return f(*arg, **kwargs)
        else:
            return redirect('/user/signup')

    return wrap

@app.route('/')
def index():
    return render_template('home.html', user="testing")

@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html', user=session['user_id'])