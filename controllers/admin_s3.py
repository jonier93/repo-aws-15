import boto3
from keys import ACCESS_KEY, SECRET_KEY
bucket_name = "bucket-aws-15"

def connectionS3():
    session_aws = boto3.Session(ACCESS_KEY, SECRET_KEY)
    session_s3 = session_aws.resource('s3')
    return session_s3

def get_file(session_s3):    
    bucket_project = session_s3.Bucket(bucket_name)
    bucket_objects = bucket_project.objects.all()
    for obj in bucket_objects:
        print(obj.key)
    print(bucket_objects)

def save_file(id, photo):
    photo_path = "/tmp/" + photo.filename
    photo.save(photo_path)
    print("Photo saved")
    return photo_path

def upload_file_s3(session_s3, photo_path):
    image_photo_s3 = "images/photo_1.jpg"
    session_s3.meta.client.upload_file(photo_path, bucket_name, image_photo_s3)
    print("Photo uploaded")
    #s3.upload_file()

