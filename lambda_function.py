import json
import boto3

def lambda_handler(event, context):
  client = boto3.client('s3')
  response = client.create_bucket(
      Bucket='mybucket-forvita123',
      )
  
