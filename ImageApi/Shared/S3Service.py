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

    def create_presigned_url(self, key, expiration=3600):

    # Generate a presigned URL for the S3 object
        s3_client = boto3.client('s3')
        response = s3_client.generate_presigned_url('get_object',
                                                        Params={'Bucket': 'info-arch-hate-images',
                                                                'Key': key},
                                                        ExpiresIn=expiration)
        return response


