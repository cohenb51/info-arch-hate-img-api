# Information Architecture - Hate Image Processing 

# Introduction
**In recent years, hate speech has become a major issue in the domain of social media. 
This paper introduces a method to detect hate speech in social media that contains hateful symbols. We first gathered hateful symbol data from different sources. This way, we created a hateful symbol dataset for this task. Then, we used this data for the training and evaluation of statistical models, which are based on state-of-the-art neural networks. Furthermore, we fine-tune pretrained descriptors that was used to define hateful symbols in our dataset. We also concluded our project by showcasing how these hateful symbols are offensive by adding expert knowledge to our trained model.** 

## Data Collection: 
** Before we dig deeper into the project, let's quickly review high level Data flow diagram that will showcase series of steps we will take to collect data via RapidAPI/BingAPI. We will label data set and further going to feature selection of the data in SageMaker Studio to train the classification model. 

![DataFlow_Final_Proj_Hate_Speech](https://user-images.githubusercontent.com/41594893/90071349-646fbf80-dcc3-11ea-9c81-41301d748235.jpeg)

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

##	Use case 3: Uploading images to API, Use Model to classify image
*	User: an external user who would like to leverage the model to predict the image as a hate symbol or otherwise
*	Scenario: As an external user, I would like to post my image via API and return a classification of that image based on a machine learning algorithmic assessment
**	General Approach:  Develop a simple CNN framework that will process an image. **
    *	A user can POST Image via the API and GET a Response
    *	The POST should contain: oAuth Credentials, the image url, request parameters (classification score, number of tags, etc.)
    *	The GET response: after processing the image, the response should return a likelihood that the image contains a hate symbol and what symbol is (swastika)

![Use_Case_3](https://user-images.githubusercontent.com/41594893/90063189-fae9b400-dcb6-11ea-9db9-3c7d3ccaa7ce.jpeg)

## 	Data model (RDMS - ERD)
![ERD_Final_Proj_Hate_Speech](https://user-images.githubusercontent.com/41594893/90071256-3db18900-dcc3-11ea-8d8f-dca9ee559146.jpeg)

## 	Architecture diagrams
![Final_Proj_Architecture](https://user-images.githubusercontent.com/41594893/90071278-45712d80-dcc3-11ea-8445-3382d02361e9.jpeg)

## Resources: 


