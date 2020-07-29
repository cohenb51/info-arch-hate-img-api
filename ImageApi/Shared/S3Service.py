import boto3
from boto.s3.key import Key
import requests
import urllib

class S3Service():
    def UploadImageFromUrl(self, key, url):
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as r:
            s3 = boto3.client('s3')
            s3.put_object(Bucket='info-arch-hate-images',Key=key,Body=r.read())
            print("upload complete")
    #todo upload img from stream
    


