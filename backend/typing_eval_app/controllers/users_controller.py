from typing_eval_app.models.users import User
from flask import jsonify, request, session, redirect, flash
from flask_bcrypt import Bcrypt
from typing_eval_app import app
from operator import itemgetter

bcrypt = Bcrypt(app)

@app.route('/register', methods=['POST'])
def register():
    fname, lname, email, pword = itemgetter("first_name", "last_name", "email", "password")(request.get_json())

    # hashing the password using bcrypt
    pw_hash = bcrypt.generate_password_hash(pword)

    # creating dictionary with user submitted information
    data = {
        "first_name" : fname,
        "last_name" : lname,
        "email" : email,
        "password" : pw_hash
    }

    # calling on save() method in User class to create User in database
    user_id = User.save(data)

    # saving the newly registered user's id in session
    session['user_id'] = user_id

    return redirect('/localhost:3000')


@app.route('/login', methods=['POST'])
def login():
    email = itemgetter("email")(request.get_json())
    # creating key - value pair with user submitted email
    data = {
        "email" : email
    }

    # retrieving user from database using the submitted email
    user_in_db = User.get_by_email(data)

    # if query to retrieve user returns false (user doesn't exist in database or email is wrong)
    if not user_in_db:
        flash(u"Invalid Email/Password", "login_error")
        return redirect('/')

    # dehashing password and checking if passwords match
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash(u"Invalid email/password", "login_error")
        return redirect('/')

    # saves the user's id in session after successful login
    session['user_id'] = user_in_db.id

    return redirect('/localhost:3000')


