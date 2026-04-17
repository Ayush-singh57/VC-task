import boto3

bucket_name = "ayush-prod-bucket-57-xyz"
region = "ap-south-1"
object_key = "documents/localfile.txt"

s3 = boto3.client("s3", region_name=region)

s3.download_file(
    bucket_name,
    object_key,
    "downloaded.txt"
)

print("File downloaded successfully")
