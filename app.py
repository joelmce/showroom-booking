from flask import Flask, render_template, session, request, flash, redirect, get_flashed_messages
from helpers.user import get_all, get_user, remove_user, add_user, get_user_by_id
from helpers.booking import get_bookings_by_user, create_booking, get_all_bookings, remove_booking
from helpers.authenticate import login_required
from sqlalchemy.orm.exc import NoResultFound
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
    flash('Test')
    create_booking(owner_id.user_id, combined)
    return {'response': "200"}

app.run(debug=True)