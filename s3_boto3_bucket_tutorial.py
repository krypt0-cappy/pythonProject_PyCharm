import boto3

aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("seconds3-boto3-bucket-2")
response = bucket.create(
    ACL='public-read',
)

print(response)
