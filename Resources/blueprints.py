from flask import Blueprint, request
from ImageApi.Models.Image import Image
import json
from ImageApi.Shared.Database.DatabaseFactory import DatabaseFactory
import configparser
from ImageApi.Shared.S3Service import S3Service


imageAccess = Blueprint('imageAccess', __name__)

@imageAccess.route('/api/')
def index():
    return "This is an example app"

@imageAccess.route('/api/image', methods = ['POST'])
def insert_image():
    data = json.loads(request.get_data())
    username, password = getCreds()
    engine = DatabaseFactory.GetDatabase("MySql", username, password)
    image = Image(Image_Url = data['ImageUrl'], Image_Id = data['ImageUrl'])
    images = []
    images.append(image)
    # engine.insert(images)
    S3Service().UploadImageFromUrl(data['ImageUrl'], data['ImageUrl'])








def getCreds():
    print("hi")
    config = configparser.ConfigParser()
    path = 'C:\\Users\\b-coh\\school\\Katz\\ImageApi\\Shared\\Configuration\\appsettings.ini'
    with open(path) as f:
        config.readfp(f)
    print(config.sections())
    username = config['connectionInfo']['username']
    password = config['connectionInfo']['password']
    return username, password
