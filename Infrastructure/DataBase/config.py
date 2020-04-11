from pymongo import MongoClient

class DataBase():
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def db_connection(self): 
        try:
            connect = MongoClient(str(self.host), str(self.port))
            print("Connected successfully to DB")
            return connect
        except:
            print("Error! Couldn't connect to DB!")
        DB = connect.database
        collection = DB.fuego
        return collection

#db = DataBase('localhost', 27017)
#db.db_connection()