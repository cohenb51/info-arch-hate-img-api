from abc import ABC, abstractmethod 
from sqlalchemy.orm import Session
from Models.User import User


class DatabaseEngine(ABC):
    def __init__(self, engine):
        self.engine = engine


    def ExecuteQuery(self, query):
        session = Session(bind = self.engine,expire_on_commit=False)
        res = session.execute(query).fetchall()
        session.close()
        return res

    def GetUser(self, userName):
        session = Session(bind = self.engine, expire_on_commit=False)
        try:
            user = session.query(User).filter(User.UserName == userName).first()
            print(user)
            session.commit()
            session.close()
            print('got user')
            return user
        except:
            session.close()
            raise 

    def insert(self, items):
        print(self)
        session = Session(bind = self.engine, expire_on_commit=False)
        try:
            session.add_all(items)
            session.commit()
            session.close()
        except:
            session.close()
            raise 