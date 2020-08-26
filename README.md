# Information Architecture - Hate Image Processing
# Introduction
**In recent years, hate speech has become a major issue in the domain of social media.
This repository introduces a way to create a platform to monitor social media for hate images. Although we looked specifically at creating a model to monitor swastikas, the ideas here can be expanded to monitor for other types of hate images.
### Method Overview
These are the steps we took in order to create our platform.
1. Data Collection - Gather Images from different sources. For this we deployed an API that posts images to s3 and stores metadata about the images in RDS. We then wrote a client that uses Rapid Api endpoints to send images.
2. Data Rating -  We created a website which users can use to log in to classify our images. This step allows us to build a supervised model with our dataset.
3. Model Building - We used our data to create a deep learning model.
4. Model Deployment - We created an endpoint that clients can call to use our model. The endpoint takes in an image and outputs a score. We also built a website that users can use over the api to directly upload an image and get a classification score.
5. Future State - Different clients can create requests to our api and raise alerts when there are hate images.
![DataFlow_Final_Proj_Hate_Speech](https://user-images.githubusercontent.com/41594893/90071349-646fbf80-dcc3-11ea-9c81-41301d748235.jpeg)
## RDS Model
This relational model is used to store the images, and classification scores
![ERD_Final_Proj_Hate_Speech](https://user-images.githubusercontent.com/41594893/91247731-f0043a00-e720-11ea-8eed-26bc877ed9df.jpeg)
Note that we chose to use a denormalized model for ease of access although in order to create multiple types of classifications this may need to be normalized.
The image_tbl stores the key of the image and the actual image is store on s3.
## Use case 1: Creating the Corpus
*	User: Internal users to create a datastore of images
*	Scenario: As an administrative user, I would like to upload images (~2,000 images or rough 4-5 GBs)  to my database in the cloud.
*	General approach: Script that loops through data sources and loads data into a scalable S3 bucket and writes metadata, S3 url path, ID, URL path of image, search parameters and timestamps, domain, file extensions to a relational database.  Each new image element should have a timestamp.
![Use_Case_1](https://user-images.githubusercontent.com/41594893/90063148-ee655b80-dcb6-11ea-84ca-82208afd122d.jpeg)
##	Use case 2: Classify image corpus through annotation/meta-tagging of images
*	User: a user who seeks to provide a database annotation along with an image
*	Scenario: As an administrative user, I would like to apply a classification to an image using prescribed tags or the addition of new tags. I would like to store my tag, and associated user metadata in a database for retrieval and analysis
*	General Approach:  create simplified administrative web page for users to review an image and store in a database their annotation and result. Basic identification would be “Does the image contain a Swastika? Yes or No?” Additional tags might include: “Does the image contain any other hate symbols and if so, what?” and what else might the image contain?”
![Use_Case_2](https://user-images.githubusercontent.com/41594893/90063183-f8875a00-dcb6-11ea-82d2-a62f3a06563a.jpeg)
These are the columns we pose on our website when making a classification.
1) Is this image hateful? 0/1
2) Does it contain Swastika? 0/1
3) Does the image contain any other hate symbol? 0/1
4) If it contain other hate symbol, then what is it? Text Answer
5) Does image contail any text/speech? 0/1
6) Is the text/speech hateful? 0/1
##	Use case 3: Uploading images to API, Use Model to classify image
*	User: an external user who would like to leverage the model to predict the image as a hate symbol or otherwise
*	Scenario: As an external user, I would like to post my image via API and return a classification of that image based on a machine learning algorithmic assessment
**	General Approach:  Develop a simple CNN framework that will process an image. **
    *	A user can POST Image via the API and GET a Response
    *	The POST should contain: oAuth Credentials, the image url, request parameters (classification score, number of tags, etc.)
    *	The GET response: after processing the image, the response should return a likelihood that the image contains a hate symbol and what symbol is (swastika)
![Use_Case_3](https://user-images.githubusercontent.com/41594893/90063189-fae9b400-dcb6-11ea-9db9-3c7d3ccaa7ce.jpeg)
## 	Architecture diagrams
![Final_Proj_Architecture](https://user-images.githubusercontent.com/41594893/90071278-45712d80-dcc3-11ea-8445-3382d02361e9.jpeg)







