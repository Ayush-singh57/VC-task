import boto3

s3 = boto3.client('s3')
BUCKET = 'ayush-final-scratch-2026-v2'
FILE_TO_DELETE = 'test_image.jpg'  
try:
    s3.delete_object(Bucket=BUCKET, Key=FILE_TO_DELETE)
    print(f"Successfully deleted {FILE_TO_DELETE} from {BUCKET}.")
except Exception as e:
    print(f"Error deleting file: {e}")