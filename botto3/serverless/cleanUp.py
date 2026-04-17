import boto3

REGION = 'ap-south-1'
LAMBDA_NAME = 'MyServerlessBackend'
API_NAME = 'MyPortfolioAPI'

def cleanup_architecture():
    apigw = boto3.client('apigatewayv2', region_name=REGION)
    lam = boto3.client('lambda', region_name=REGION)
    
    # 1. Delete API Gateway
    try:
        print("Searching for API Gateway...")
        apis = apigw.get_apis()['Items']
        for api in apis:
            if api['Name'] == API_NAME:
                apigw.delete_api(ApiId=api['ApiId'])
                print(" API Gateway deleted.")
    except Exception as e:
        print(f"Error deleting API: {e}")

    # 2. Delete Lambda
    try:
        print("Deleting Lambda function...")
        lam.delete_function(FunctionName=LAMBDA_NAME)
        print(" Lambda function deleted.")
    except lam.exceptions.ResourceNotFoundException:
        print(" Lambda function already deleted.")
    except Exception as e:
        print(f"Error deleting Lambda: {e}")

if __name__ == "__main__":
    cleanup_architecture()