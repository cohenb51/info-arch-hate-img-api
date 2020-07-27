from .MySqlEngine import MySqlEngine

class DatabaseFactory():
    @staticmethod
    def GetDatabase(database_type, username, password):
        if(database_type == 'MySql'):
            return MySqlEngine(username, password)
