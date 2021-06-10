from flask import flash, jsonify
from ..config.mysqlconnection import connectToMySQL
from ..models.stats import Stat
import re, json

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.stats = []

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
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users LEFT JOIN stats ON users.id = stats.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL("typing_eval_db").query_db(query, data)
        data = {
            "id" : results[0]['id'],
            "username" : results[0]['username'],
            "email" : results[0]['email'],
            "password" : results[0]['password'],
            "created_at" : str(results[0]['created_at']),
            "updated_at" : str(results[0]['updated_at']),
            "stats" : []
        }
        user = cls(data)

        for row in results:
            # grabbing stats data according to the row's stats.id
            stat = Stat.get_one({"id":row['stats.id']})
            # adding it to list of stats in User object
            user.stats.append(stat)

        return user
    