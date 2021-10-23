import boto3
import botocore
from botocore.config import Config
import hmac
import base64
import hashlib

# Fill these
username = ''
password = ''
clientid = ''
clientsecret = ''
userpoolid = ''
region = ''

config = Config(signature_version=botocore.UNSIGNED)
client = boto3.client('cognito-idp', config=config, region_name=region)

def hmacdigest(username, clientid, clientsecret):
    message = username + clientid
    dig = hmac.new(bytes(clientsecret, 'UTF-8'), msg=message.encode('UTF-8'), digestmod=hashlib.sha256).digest()    
    return base64.b64encode(dig).decode()

digest = hmacdigest(username, clientid, clientsecret)

response = client.initiate_auth(
    ClientId= clientid,
    AuthFlow='USER_PASSWORD_AUTH',
    AuthParameters={
        'USERNAME': username,
        'PASSWORD': password,
        'SECRET_HASH': digest
    }
)

print(response['AuthenticationResult']['IdToken'])
