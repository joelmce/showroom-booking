from flask import Flask, render_template, session, request, flash, redirect
from models.user import get_all, get_user, remove_user, add_user
from helpers.authenticate import is_admin, login_required
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
import os

app = Flask(__name__)
app.secret_key = "Magically"

@app.route("/")
def index():
    user = ""
    if session.get("user"):
        user_session = session['user']
        user = get_user(user_session)
    return render_template("index.html.jinja", user=user)

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

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

@app.route("/admin")
@login_required
def admin():
    all_users = get_all()
    return render_template("admin.html.jinja", users=all_users)

@app.route("/user/delete/<id>")
@login_required
def delete_user(id):
    remove_user(id)
    return redirect("/admin")

@app.route('/user/new')
@login_required
def new_user_form():
    return render_template("new_user.html.jinja")

@app.route('/user/new', methods=['POST'])
@login_required
def new_user_action():
    name = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    admin = bool(request.form.get("admin"))

    add_user(name, email, password, admin)    
    return redirect("/admin")

app.run(debug=True, port=5000)
