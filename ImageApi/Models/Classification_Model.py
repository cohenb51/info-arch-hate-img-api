from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from PIL import Image as Img
import requests
from io import BytesIO
from urllib.parse import urlparse
from datetime import datetime
import json
import urllib.parse


Base = declarative_base()

class Classification_Score_Model(Base):
    __tablename__ = "Image_Classification_Score_tbl"
    Classification_Ccore_Id = Column(String, primary_key = True)
    Image_Id = Column(String)
    Username = Column(String)
    Score = Column(Integer)

    def as_dict(self):
       _dict =  {c.name: getattr(self, c.name) for c in self.__table__.columns}
       tmp = _dict['Image_Id']
       _dict['Image_Id'] ='https://info-arch-hate-images-corp.s3.amazonaws.com/' +  urllib.parse.quote(tmp)
       return _dict