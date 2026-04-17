import boto3
from botocore.config import Config
import webbrowser

# -----------------------------
# Configuration
# -----------------------------
bucket_name = "ayush-prod-bucket-57-xyz"
region = "ap-south-1"
object_key = "documents/localfile.txt"

# Force correct region + signature version
config = Config(
    region_name=region,
    signature_version="s3v4"
)

s3 = boto3.client("s3", config=config)

print("Using region:", s3.meta.region_name)

# -----------------------------
# Upload file
# -----------------------------
s3.upload_file(
    "localfile.txt",
    bucket_name,
    object_key
)

print("Upload successful")

# -----------------------------
# Generate presigned URL
# -----------------------------
url = s3.generate_presigned_url(
    ClientMethod="get_object",
    Params={
        "Bucket": bucket_name,
        "Key": object_key
    },
    ExpiresIn=300,
    HttpMethod="GET"
)

# Save URL to file (to avoid terminal wrapping issues)
with open("presigned_url.txt", "w") as f:
    f.write(url)

print("\nPresigned URL saved to presigned_url.txt")

# Automatically open in browser
webbrowser.open(url)
