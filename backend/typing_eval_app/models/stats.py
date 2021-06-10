from flask import flash
from ..config.mysqlconnection import connectToMySQL

class Stat:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.score = data['score']
        self.wpm = data['wpm']
        self.accuracy = data['accuracy']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO stats (user_id, wpm, accuracy, backspace_count, created_at, updated_at) VALUES (%(user_id)s, %(wpm)s, %(accuracy)s, %(backspace_count)s, NOW(), NOW());"
        new_score_id = connectToMySQL("typing_eval_db").query_db(query, data)
        return new_score_id

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM stats WHERE stats.id = %(id)s;"
        result = connectToMySQL("typing_eval_db").query_db(query, data)
        return result[0]
    
    @classmethod
    def update(cls, data):
        query = "UPDATE stats SET user_id = %(user_id)s WHERE stats.id = %(id)s;"
        result = connectToMySQL("typing_eval_db").query_db(query, data)
        return result[0]
    
    