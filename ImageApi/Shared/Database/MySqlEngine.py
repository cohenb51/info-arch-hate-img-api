import configparser
from sqlalchemy import create_engine
from .DatabaseEngine import DatabaseEngine
import os

class MySqlEngine(DatabaseEngine):

    def __init__(self,username,password):
        config = configparser.ConfigParser()
        path = os.path.join("Shared", "Configuration", "appsettings.ini")
        with open(path) as f:
            config.readfp(f) 
        host = config['connectionInfo']['host']
        port = config['connectionInfo']['port']
        dbName = config['connectionInfo']['dbname']


        connectionString = 'mysql+pymysql://%s:%s@%s:%s/%s' % (
        username,
        password,
        host,
        port,
        dbName)
        print("connection string")
        print(connectionString)
        sqlEngine  = create_engine(connectionString, pool_recycle=3600)

        super().__init__(create_engine(connectionString))