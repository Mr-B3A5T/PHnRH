from flask import Blueprint, render_template, redirect, request

login = Blueprint('login', __name__)

@login.route('/')
def index():
    return render_template('login.html')

@login.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == 'admin' and password == 'password':
        return redirect('/dashboard')
    else:
        return redirect('/')
