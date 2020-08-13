from abc import ABC, abstractmethod 
from sqlalchemy.orm import Session
from Models.User import User
from Models.Classification_Model import Classification_Score_Model


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

    def GetAllImages(self):
        session = Session(bind = self.engine, expire_on_commit=False)
        try:
            images = list(session.query(Classification_Score_Model))
            print(type(images))
            print("type")
            session.commit()
            session.close()
            print('got all images')
            print(images[0].Image_Id)
            return images
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

    def InsertClassificationScore(self, score, url, user):
        try:
            conn = self.engine.raw_connection()
            cursor = conn.cursor()
            cursor.callproc("ScoreImage_prc", [url, score, 1, user])
            results = list(cursor.fetchall())
            print("got results")
            print(url)
            print(results)
            cursor.close()
            conn.commit()
        finally:
                conn.close() 


