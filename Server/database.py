import mysql.connector
from flask_login import UserMixin


class Database():

    def __init__(self, name='test1'):
        connection = mysql.connector.connect(
        host='localhost',
        database=name,
        user='root',
        password='root',
        auth_plugin='mysql_native_password')
        
        self.connection = connection
        
    def close(self):
        self.connection.close()
    


class User(UserMixin):
    
    def __init__(self, userName, email, phoneNumber):
        self.id = userName
        self.email = email
        self.phoneNumber = phoneNumber
        
    def __repr__(self):
        return f"userName: {self.id}"
    
    def create_user(id):
        db = Database()
        cur = db.connection.cursor()
        cur.execute(f"SELECT * FROM ACCOUNTS WHERE accID = '{id}' OR email = '{id}'")
        userData = cur.fetchone()
        userName = userData[0]
        email = userData[1]
        phoneNumber = userData[3]
        db.close()
        
        user = User(userName, email, phoneNumber)
        return user 
    

class QueryContainer():

    def __init__(self):
        self.query = ''       
    
    def registerQuery(self, query):
        self.query = query
    
    def clearLastQuery(self):
        self.query = ''

    def executeInsertQuery(self):
        db = Database('test1')
        cur = db.connection.cursor()
        cur.execute(self.query)
        db.connection.commit()
        db.close()
        self.clearLastQuery()
        



