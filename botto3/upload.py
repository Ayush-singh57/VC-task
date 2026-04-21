import boto3
from botocore.config import Config
import webbrowser
 
bucket_name = "ayush-prod-bucket-57-xyz"
region = "ap-south-1"
object_key = "documents/localfile.txt"

config = Config(
    region_name=region,
    signature_version="s3v4"
)

s3 = boto3.client("s3", config=config)

print("Using region:", s3.meta.region_name)
 
s3.upload_file(
    "localfile.txt",
    bucket_name,
    object_key
)

print("Upload successful")

url = s3.generate_presigned_url(
    ClientMethod="get_object",
    Params={
        "Bucket": bucket_name,
        "Key": object_key
    },
    ExpiresIn=300,
    HttpMethod="GET"
)
  
with open("presigned_url.txt", "w") as f:
    f.write(url)

print("\nPresigned URL saved to presigned_url.txt")
 
webbrowser.open(url)
