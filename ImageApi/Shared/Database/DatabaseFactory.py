from .MySqlEngine import MySqlEngine
import configparser
import os


class DatabaseFactory():
    @staticmethod
    def GetDatabase(database_type, username, password):
        global engine
        if(database_type == 'MySql'):
            engine = MySqlEngine(username, password)
            return engine

def GetCreds():
    config = configparser.ConfigParser()
    path = os.path.join("Shared", "Configuration", "appsettings.ini")
    with open(path) as f:
        config.readfp(f)
    username = config['connectionInfo']['username']
    password = config['connectionInfo']['password']
    return username, password

username,password = GetCreds()
engine = DatabaseFactory.GetDatabase("MySql", username, password)


