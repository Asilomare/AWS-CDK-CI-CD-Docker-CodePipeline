import requests
from bs4 import BeautifulSoup
import boto3
import json

s3 = boto3.client('s3')
def lambda_handler(event, context):
    URL = "https://www.worldometers.info/coronavirus/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.findAll("div", class_='maincounter-number')
    
    bucket = 'webscraperbucket123123'
    
    transcationToUpload = {}
    transcationToUpload['cases'] = results[0].text
    transcationToUpload['deaths'] = results[1].text
    transcationToUpload['recovered'] = results[2].text
    
    file_name = 'data' + '.json'
    uploadByteStream = bytes(json.dumps(transcationToUpload).encode('UTF-8'))
    
    s3.put_object(Bucket=bucket, Key=file_name, Body=uploadByteStream)
