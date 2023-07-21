from flask import Flask, render_template, session, request, flash, redirect, get_flashed_messages
from helpers.user import get_all, get_user, remove_user, add_user, get_user_by_id, edit_user
from helpers.booking import get_bookings_by_user, get_booking_owner, create_booking, get_all_bookings, remove_booking, get_booking, edit_booking
from helpers.authenticate import login_required, checkpassword, hashpassword, login_user

from helpers.emails import send_email

app = Flask(__name__)
app.secret_key = "Magically"

@app.route("/")
def index():
    user = ""
    if session.get("user"):
        user_session = session['user']
        user = get_user(user_session)
    else:
        return redirect("/login")    
    return render_template("index.html.jinja", user=user)

@app.route("/login")
def login():
    if session.get("user"):
        return redirect("/")
    return render_template("login.html.jinja")

@app.route('/login/success', methods=['POST'])
def login_success():
    name = request.form.get('username')
    pw = request.form.get('password')
    login_user(get_user(name), pw)
    return redirect("/")       


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

@app.route("/user/<id>")
def user(id):
    bookings = get_bookings_by_user(id)
    user = get_user_by_id(id)
    return render_template("user.html.jinja", user=user, bookings=bookings)

@app.route("/admin")
@login_required
def admin():
    all_users = get_all()
    all_bookings = get_all_bookings()
    return render_template("admin.html.jinja", users=all_users, bookings=all_bookings)

@app.route("/user/delete/<id>")
@login_required
def delete_user(id):
    remove_user(id)
    return redirect("/admin")

@app.route('/booking/delete/<id>')
@login_required
def delete_booking(id):
    remove_booking(id)
    return redirect('/admin')

@app.route("/booking/<id>")
@login_required
def view_booking(id):
    booking = get_booking(id)
    name = get_booking_owner(1)
    return render_template("booking.html.jinja", booking=booking, name=name)

@app.route("/booking/<id>/comments/add", methods=['POST'])
@login_required
def add_comments(id):
    comment = request.form.get("comments")
    edit_booking(id, "comments", comment)
    return redirect(f"/booking/{id}")

@app.route('/change-password')
@login_required
def change_password():
    user = get_user(session.get("user"))
    return render_template("change-password.html.jinja", user=user)

@app.route("/change-password/success", methods=['POST'])
@login_required
def change_password_handler():
    id = request.form.get("id")
    old_password = request.form.get("old-password") # TODO: Check to see if old_password is correct
    new_password = request.form.get("new-password")
    edit_user(id, "password", new_password)
    return redirect("/")

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

@app.route("/book", methods=['POST'])
def new_booking():
    owner_id = get_user(session.get('user',''))
    booking = request.get_json()
    dates = str(booking['date'])
    time = str(booking['time'])
    combined = dates + " " + time
    create_booking(owner_id.user_id, combined)
    return {'response': "200"}
