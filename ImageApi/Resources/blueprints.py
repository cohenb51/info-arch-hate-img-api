from flask import Blueprint, request
from Models.Image import Image, GetImage
import json
from Shared.Database.DatabaseFactory import DatabaseFactory, engine
from Shared.S3Service import S3Service
import os
from flask import render_template



imageAccess = Blueprint('imageAccess', __name__)

@imageAccess.route('/api/')
def index():
    return "This is an example app"

@imageAccess.route('/api/image', methods = ['POST'])
def insert_image():
    data = json.loads(request.get_data())
    image = GetImage(data['ImageUrl'])
    images = []
    images.append(image)
    engine.insert(images)
    S3Service().UploadImageFromUrl(image.Image_Id, image.Image_Url)
    return json.dumps({'success':True}), 201, {'ContentType':'application/json'} 

@imageAccess.route('/api/image', methods = ['GET'])
def get_image():
    url = GetImageFromAws()
    return render_template('image.html', url =url )

def GetImageFromAws():
    key = engine.ExecuteQuery('CALL GetImage_prc')
    url = S3Service().create_presigned_url(key[0]['Image_Id'])
    return url


