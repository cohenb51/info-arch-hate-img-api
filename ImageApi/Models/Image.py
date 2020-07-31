from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from PIL import Image as Img
import requests
from io import BytesIO
from urllib.parse import urlparse
from datetime import datetime


Base = declarative_base()

class Image(Base):
    __tablename__ = "Image_tbl"
    Image_Id = Column(String, primary_key = True)
    Image_Url = Column(String)
    Height = Column(Integer)
    Width = Column(Integer)
    HostName = Column(String)


def GetImage(url):
    response = requests.get(url)
    image = Img.open(BytesIO(response.content)) # will fail if not an image although should decouple at some point.
    parsed_uri = urlparse(url)
    host = parsed_uri.netloc
    key = f'{datetime.today().strftime("%Y-%m-%d")}//{parsed_uri.netloc}//{parsed_uri.path}'
    print(key)
    print("key")
    print(host)
    image = Image(
        Image_Id = key,
        Image_Url = url,
        Height = image.height,
        Width = image.width,
        HostName = host)
    return image
