import boto3

region = "ap-south-1"
bucket_name = "ayush-prod-bucket-57-xyz"

s3 = boto3.client("s3", region_name=region)

# 1. Create bucket
s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        "LocationConstraint": region
    }
)

print("Bucket created")

# 2. Enable versioning
s3.put_bucket_versioning(
    Bucket=bucket_name,
    VersioningConfiguration={
        "Status": "Enabled"
    }
)

print("Versioning enabled")
