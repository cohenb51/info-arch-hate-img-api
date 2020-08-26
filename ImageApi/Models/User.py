from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from PIL import Image as Img
from Shared.SaltService import SaltService

Base = declarative_base()

class User(Base):
    __tablename__ = "User_tbl"
    UserName = Column(String, primary_key = True)
    Password = Column(String)

def GetUser(username, password):
    password_r = SaltService(). GetHashedPassword(password)
    return User(UserName = username, Password = password_r)
    
