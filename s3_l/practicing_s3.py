import boto3
import os
from boto3.s3.transfer import TransferConfig

# 1. Initialize S3 Client
s3 = boto3.client('s3')
BUCKET_NAME = 'ayush-deep-dive-lab'

def run_lab():
    # --- ACTION: Create Bucket ---
    print("Step 1: Creating Bucket...")
    s3.create_bucket(Bucket=BUCKET_NAME, CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})

    # --- SCENARIO: Multipart Upload (Simulated for practice) ---
    print("Step 2: Uploading file with Multipart Config...")
    config = TransferConfig(multipart_threshold=1024 * 5, max_concurrency=5) # 5MB threshold
    # Create a dummy file
    with open("test_image.jpg", "wb") as f:
        f.write(os.urandom(1024 * 6)) # 6MB file to trigger multipart
    
    s3.upload_file("test_image.jpg", BUCKET_NAME, "uploads/user_image.jpg", Config=config)

    # --- SCENARIO: Generate Presigned URL ---
    print("Step 3: Generating temporary link...")
    url = s3.generate_presigned_url(
        'get_object', 
        Params={'Bucket': BUCKET_NAME, 'Key': 'uploads/user_image.jpg'}, 
        ExpiresIn=60 # Valid for 60 seconds
    )
    print(f"\nClick this link to see your file (expires in 1 min):\n{url}\n")

    # --- ACTION: Set Lifecycle Rule ---
    print("Step 4: Setting Lifecycle Policy to Archive after 30 days...")
    s3.put_bucket_lifecycle_configuration(
        Bucket=BUCKET_NAME,
        LifecycleConfiguration={
            'Rules': [{
                'ID': 'ArchiveLogic',
                'Status': 'Enabled',
                'Filter': {'Prefix': 'uploads/'},
                'Transitions': [{'Days': 30, 'StorageClass': 'GLACIER'}]
            }]
        }
    )

if __name__ == "__main__":
    run_lab()