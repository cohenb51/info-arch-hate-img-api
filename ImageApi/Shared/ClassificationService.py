from Shared.S3Service import S3Service
import keras
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image as Img
import os

models = []
testModelName = 'primitive_model.h5'
modelFile = S3Service().GetObject('info-arch-hate-images-train-stage', 'primitive_model.h5')
print(os.listdir('static'))
models.append(load_model(f'static/{testModelName}'))


class ClassificationResponse():
    def __init__(self):
        self.scoreObjects = []


class ClassificationService():
    def Classify(self, image): 
        images = []
        images.append(image)
        return self.ClassifyList(images)

    def ClassifyList(self, images):
        listOfImages = []
        for image in images:
            openedImage = Img.open(image)
            imageArray = self.preprocess(openedImage)
            listOfImages.append(imageArray)
        scores = []
        for model in models:
            arr = np.array(listOfImages)
            print('shape')
            print(arr.shape)
            scores.append(model.predict_classes(arr))
            return self.scoresToClassificationResponse(models, scores)

    def preprocess(self, image):
        tmp = np.asarray(image.convert('RGB').resize((64,64)))
        print('tmp')
        print(tmp.shape)
        return tmp

    def scoresToClassificationResponse(self, models, scores):
        response = ClassificationResponse()
        for i in range(len(scores)):
            score = 'IsSwastika' if scores[i] == 1 else 'NotASwastika'
            data = {'model':i, 'score':score}
            response.scoreObjects.append(data)
            print('score')
        print(len(scores))
        return response

