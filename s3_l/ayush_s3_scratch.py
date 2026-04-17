import boto3
from botocore.config import Config
from botocore.exceptions import ClientError

# --- CONFIGURATION ---
REGION = 'ap-south-1' # Mumbai
BUCKET_NAME = 'ayush-final-scratch-2026-v2' # Changed slightly to ensure a fresh run
LOCAL_FILE = 'my_photo.png'
S3_KEY = 'uploads/my_photo.png'

# 1. Force Signature Version 4 
s3_config = Config(
    region_name = REGION,
    signature_version = 's3v4'
)

# 2. Initialize the client
s3 = boto3.client('s3', config=s3_config)

def run_full_s3_flow():
    try:
        # --- CREATE BUCKET ---
        print(f"Creating bucket '{BUCKET_NAME}'...")
        s3.create_bucket(
            Bucket=BUCKET_NAME,
            CreateBucketConfiguration={'LocationConstraint': REGION}
        )

        # --- UPLOAD PNG ---
        print(f"Uploading '{LOCAL_FILE}'...")
        s3.upload_file(
            LOCAL_FILE, 
            BUCKET_NAME, 
            S3_KEY,
            ExtraArgs={'ContentType': 'image/png'}
        )

        # --- LIST OBJECTS ---
        print("\nVerifying files in bucket:")
        response = s3.list_objects_v2(Bucket=BUCKET_NAME)
        for obj in response.get('Contents', []):
            print(f" - Found: {obj['Key']} ({obj['Size']} bytes)")

        # --- GENERATE SECURE VIEW LINK ---
        url = s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': BUCKET_NAME, 'Key': S3_KEY},
            ExpiresIn=3600 
        )
        print(f"\nSUCCESS! Click this link to view your image:\n{url}")

    except ClientError as e:
        print(f"AWS Error: {e.response['Error']['Message']}")
    except FileNotFoundError:
        print(f"Error: Could not find '{LOCAL_FILE}' in your folder.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_full_s3_flow()