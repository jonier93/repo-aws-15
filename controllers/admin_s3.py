import boto3
ACCESS_KEY = 'AKIASVQKHNJLOL74LJCF'
SECRET_KEY = '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'

def connectionS3():
    session_aws = boto3.Session(ACCESS_KEY, SECRET_KEY)
    print(session_aws)

connectionS3()