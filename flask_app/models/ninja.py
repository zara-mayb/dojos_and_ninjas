from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        return results
        
    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas ( dojo_id, first_name, last_name ) VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s);"
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        return results
