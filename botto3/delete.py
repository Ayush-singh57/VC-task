import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('ayush-prod-bucket-57-xyz')

bucket.objects.all().delete()

bucket.delete()

print("Bucket is successfully deleted")