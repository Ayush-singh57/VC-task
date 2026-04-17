import boto3

bucket_name = "ayush-prod-bucket-57-xyz"
region = "ap-south-1"

s3 = boto3.client("s3", region_name=region)

response = s3.list_objects_v2(Bucket=bucket_name)

for obj in response.get("Contents", []):
    print("Found object:", obj["Key"])
