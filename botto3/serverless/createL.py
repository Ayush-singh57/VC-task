import boto3
import zipfile
import io

REGION = 'ap-south-1'
FUNCTION_NAME = 'MyServerlessBackend'
ROLE_ARN = 'arn:aws:iam::835637956758:role/practice'

def deploy_backend():
    lambda_client = boto3.client('lambda', region_name=REGION)
    
    lambda_code = """
import json

def lambda_handler(event, context):
    print("Lambda triggered!")
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Hello from a single-file deployment!"})
    }
"""
    
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w') as z:
        z.writestr('index.py', lambda_code)
        
    print("Deploying Lambda function...")
    try:
        lambda_client.create_function(
            FunctionName=FUNCTION_NAME,
            Runtime='python3.12',
            Role=ROLE_ARN,
            Handler='index.lambda_handler',
            Code={'ZipFile': buf.getvalue()},
            Timeout=10,
            MemorySize=128
        )
        print(" Lambda function created ")
        
    except lambda_client.exceptions.ResourceConflictException:
        print("Lambda function already exists. Delete it first if you want to recreate it.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    deploy_backend()