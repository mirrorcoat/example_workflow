from flask import Flask, session, redirect, url_for

class User:
    def __init__(self, username, password):
        self.id = 0 # this would normally hold the user's uuid and be used to grab user information when needed
        self.username = username
        self.password =  password

    def start_session(self):
        session['logged_in'] = True
        session['user_id'] = self.username

        return redirect(url_for('dashboard'))
