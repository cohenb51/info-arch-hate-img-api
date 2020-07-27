from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Image(Base):
    __tablename__ = "Image_tbl"
    Image_Id = Column(String, primary_key = True)
    Image_Url = Column(String)