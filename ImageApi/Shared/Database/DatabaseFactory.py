from .MySqlEngine import MySqlEngine

engine = None
class DatabaseFactory():
    @staticmethod
    def GetDatabase(database_type, username, password):
        global engine
        if(database_type == 'MySql'):
            if (engine):
                return engine
            engine = MySqlEngine(username, password)
            return engine
