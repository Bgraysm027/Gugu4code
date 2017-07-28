import boto3
rekog=boto3.client('rekognition')
response=rekog.recognize_celebrities(
    Image={

        'S3Object': {
            'Bucket': 'bgs-kognition',
            'Name': 'Gugu.jpg'
        }
    }
)

print(response)
