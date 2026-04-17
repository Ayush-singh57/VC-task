import boto3

s3 = boto3.client("s3", region_name="ap-south-1")
bucket_name = "ayush-prod-bucket-57-xyz"

response = s3.list_objects_v2(Bucket=bucket_name)

for obj in response.get("Contents", []):
    print("Object:", obj["Key"])
