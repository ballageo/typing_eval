from flask import flash
from ..config.mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.scores = []

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['username']) < 2:
            flash("Username must be at least 2 characters", "username")
            is_valid = False
        if len(user['password']) < 2:
            flash("Password must be at least 8 characters", "password")
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash("Passwords do not match", "password")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address", "email")
            is_valid = False
        return is_valid

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        new_user = connectToMySQL("typing_eval_db").query_db(query, data)
        print(new_user)
        return new_user
    
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("typing_eval_db").query_db(query, data)
        print(result)
        if len(result) < 1:
            return False
        return cls(result[0])
    