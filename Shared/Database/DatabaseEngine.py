from abc import ABC, abstractmethod 
from sqlalchemy.orm import Session


class DatabaseEngine(ABC):
    def __init__(self, engine):
        self.engine = engine


    def ExecuteQuery(query):
        session - Session(bind = self.engine)
        res = session.execute(query).fetchall()
        session.close()
        return res

    def insert(self, items):
        print(self)
        session = Session(bind = self.engine)
        print(len(items))
        session.add_all(items)
        session.commit()
        session.close