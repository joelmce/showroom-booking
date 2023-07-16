from flask import Flask, render_template, session, request, flash, redirect
from models.user import get_all, User, get_user
from helpers.authenticate import is_admin, login_required
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
import os

app = Flask(__name__)
app.secret_key = "Magically"

@app.route("/")
def index():
    results = get_all()
    user_session = session['user']
    return render_template("index.html.jinja", results=results, user=user_session)

@app.route("/login")
def login():
    return render_template("login.html.jinja")

@app.route('/login/success', methods=['POST'])
def handle_login():
    name = request.form.get('username')
    pw = request.form.get('password')
    fetched_user = get_user(name)
    print(fetched_user.name)

    try:
        if fetched_user is not None:
            # password_check = bcrypt.checkpw(pw.encode(), fetched_user.password.encode())
            if pw == fetched_user.password:
                session['user'] = fetched_user.name
                session['admin'] = fetched_user.admin
                return redirect("/")
        else:
            print(f"No fetched user found. Returned: {fetched_user}")    
    except NoResultFound:
        flash("User does not exist")
    print(session['admin'])    
    return redirect("/")   

@app.route("/admin")
@login_required
def admin(user):
    user_perms = session.get('admin', '')
    print(user_perms)
    if user_perms:
        return "Authenticated"
    else:
        return redirect("/")

app.run(debug=True)
