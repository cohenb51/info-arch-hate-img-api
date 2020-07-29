from flask import Blueprint, request
from Models.Image import Image, GetImage
import json
from Shared.Database.DatabaseFactory import DatabaseFactory
import configparser
from Shared.S3Service import S3Service
import os


imageAccess = Blueprint('imageAccess', __name__)

@imageAccess.route('/api/')
def index():
    return "This is an example app"

@imageAccess.route('/api/image', methods = ['POST'])
def insert_image():
    data = json.loads(request.get_data())
    username, password = getCreds()
    engine = DatabaseFactory.GetDatabase("MySql", username, password)
    image = GetImage(data['ImageUrl'])
    images = []
    images.append(image)
    engine.insert(images)
    S3Service().UploadImageFromUrl(image.Image_Id, image.Image_Url)
    return json.dumps({'success':True}), 201, {'ContentType':'application/json'} 


def getCreds():
    config = configparser.ConfigParser()
    path = os.path.join("Shared", "Configuration", "appsettings.ini")
    with open(path) as f:
        config.readfp(f)
    username = config['connectionInfo']['username']
    password = config['connectionInfo']['password']
    return username, password
