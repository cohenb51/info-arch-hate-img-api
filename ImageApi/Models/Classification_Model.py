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
    __tablename__ = "Image_Classification_Scores_tbl"
    Num = Column(Integer, primary_key = True)
    key = Column(String)
    IsHatefull = Column(Integer)
    HasSwastika = Column(String)
    HasOtherHateSymbol =Column(String)
    HateImage = Column(String)
    HasText = Column(String)
    HasHatefullText = Column(String)
    HasOtherHateSymbol = Column(String)

    def as_dict(self):
       _dict =  {c.name: getattr(self, c.name) for c in self.__table__.columns}
       tmp = _dict['key']
       _dict['url'] ='https://info-arch-hate-images-corp.s3.amazonaws.com/' +  urllib.parse.quote(tmp)
       return _dict