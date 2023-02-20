
#For input use postman app to check for this api and provide json data as input

import boto3

def lambda_handler(event, context):
    # TODO implement
    s3 = boto3.client('s3')
    bucket = 'bucket-name'
    key = 'filename.txt'
    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body'].read().decode('utf-8')
    print(content)
    return {
        'statusCode': 200,
        'body': content
    }
