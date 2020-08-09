from flask import Blueprint, request
from Models.Image import Image, GetImage
from Models.User import User, GetUser
import json
from Shared.Database.DatabaseFactory import DatabaseFactory, engine
from Shared.S3Service import S3Service
from Shared.SaltService import SaltService
import os
from flask import render_template, session
from flask_api import status




imageAccess = Blueprint('imageAccess', __name__)

@imageAccess.route('/api/')
def index():
    return "This is an example app"

@imageAccess.route('/api/image', methods = ['POST'])
def insert_image():
    if 'username' not in session:
        return json.dumps({'status': 'User is not logged in.'}),status.HTTP_403_FORBIDDEN
    data = json.loads(request.get_data())
    image = GetImage(data['ImageUrl'])
    images = []
    images.append(image)
    engine.insert(images)
    S3Service().UploadImageFromUrl(image.Image_Id, image.Image_Url)
    return json.dumps({'success':True}), 201, {'ContentType':'application/json'} 

@imageAccess.route('/api/unclassifiedimage', methods = ['GET'])
def get_image():
    if 'username' not in session:
        return json.dumps({'status': 'User is not logged in.'}),status.HTTP_403_FORBIDDEN
    url = GetImageFromAws()
    return render_template('image.html', url =url )

@imageAccess.route('/api/register', methods = ['Post'])
def register_user():
    data = json.loads(request.get_data())
    user = GetUser(data['UserName'], data['Password'])
    users = []
    users.append(user)
    engine.insert(users)
    return json.dumps({'success':True}), 201, {'ContentType':'application/json'} 

@imageAccess.route('/api/logout', methods = ['Post'])
def logout():
    if 'username' not in session:
        return json.dumps({'status': 'User is not logged in.'}),status.HTTP_403_FORBIDDEN
    else:
        session.pop('username')
    return json.dumps({'success':True}), 201, {'ContentType':'application/json'} 

@imageAccess.route('/api/login', methods = ['Post'])
def login():
    data = json.loads(request.get_data())
    user = GetUserFromDb(data['UserName'], data['Password'])
    if(user):
        session['username'] = user.UserName
        return json.dumps({'status': 'f{user.UserName} logged in'}), 200, {'ContentType':'application/json'} 
    else:
        return json.dumps({'status': 'user and password combination not found'}),status.HTTP_403_FORBIDDEN

def GetImageFromAws():
    key = engine.ExecuteQuery('CALL GetImage_prc')
    url = S3Service().create_presigned_url(key[0]['Image_Id'])
    return url

def GetUserFromDb(username, password):
    user = engine.GetUser(username)
    if(user):
        if(SaltService().ValidatePassword(password, user.Password)):
            return user
    return 



