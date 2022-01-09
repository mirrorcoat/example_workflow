from user.models import User
from app import app
from flask import request, session, render_template

valid_logins = ['ben', 'nemanja', 'password']
# valid_passwords should hold a list of valid_passwords

@app.route('/user/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        # Validate user 
        if request.form.get('username') in valid_logins:
            user = User(request.form.get('username'), request.form.get('password'))
            return user.start_session()
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/user/signout', methods=['GET'])
def signout():
    session.clear()
    return render_template('home.html')