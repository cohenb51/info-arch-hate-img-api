from flask import Blueprint, request
from Models.Image import Image, GetImage
from Models.User import User, GetUser
from Models.Classification_Model import  Classification_Score_Model
import json
from Shared.Database.DatabaseFactory import DatabaseFactory, engine
from Shared.S3Service import S3Service
from Shared.SaltService import SaltService
import os
from flask import render_template, session, redirect, url_for, jsonify
from flask_api import status




imageAccess = Blueprint('imageAccess', __name__)

@imageAccess.route('/api/')
def index():
    return "This is an example app"

@imageAccess.route('/api/image', methods = ['POST'])
def insert_image():
    if 'username' not in session:
        return render_template('login.html')
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
        return redirect(url_for('imageAccess.login_screen'))
    url = GetImageFromAws()
    return render_template('image.html', url =url[0], key=url[1] )

@imageAccess.route('/api/unclassifiedimage', methods = ['POST'])
def post_image():
    print(type(request.form['id']))
    print(request.form['id'])
    print('form')
    if 'username' not in session:
        return redirect(url_for('imageAccess.login_screen'))

    post_score_to_db(request.form['classification'], request.form['id'], session['username'] )
    url = GetImageFromAws()
    return redirect(url_for('imageAccess.get_image'))

def post_score_to_db(score, url, username):
    engine.InsertClassificationScore(score, url, username)



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
    # data = json.loads(request.get_data())
    user = GetUserFromDb(request.form['UserName'], request.form['Password'])
    if(user):
        session['username'] = user.UserName
        return redirect(url_for('imageAccess.get_image')) 
    else:
        return render_template('login.html', error = "credentials not found")


@imageAccess.route('/api/login', methods = ['Get'])
def login_screen():
    return render_template('login.html')

@imageAccess.route('/api/allImages', methods = ['Get'])
def GetAllImages():
    images = engine.GetAllImages()
    dicts = list(map(lambda x: x.as_dict(), images))
    return (jsonify(dicts)), 200, {'ContentType':'application/json'}
    
def GetImageFromAws():
    key = engine.ExecuteQuery('CALL GetImage_prc')
    url = S3Service().create_presigned_url(key[0]['Image_Id'])
    return url, key[0]['Image_Id']

def GetUserFromDb(username, password):
    user = engine.GetUser(username)
    if(user):
        if(SaltService().ValidatePassword(password, user.Password)):
            return user
    return 
