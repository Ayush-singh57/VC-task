import boto3

REGION = 'ap-south-1'
LAMBDA_NAME = 'MyServerlessBackend'
API_NAME = 'MyPortfolioAPI'

def create_public_endpoint():
    apigw = boto3.client('apigatewayv2', region_name=REGION)
    lam = boto3.client('lambda', region_name=REGION)
    sts = boto3.client('sts') # Added to fetch Account ID

    print("Fetching Lambda details...")
    try:
        # Get the Amazon Resource Name (ARN) of our Lambda
        lambda_info = lam.get_function(FunctionName=LAMBDA_NAME)
        lambda_arn = lambda_info['Configuration']['FunctionArn']
    except Exception as e:
        print(f"Error finding Lambda. Did you run script 02 first? {e}")
        return

    print("Creating API Gateway...")
    try:
        # Create an HTTP API and instantly route it to our Lambda
        api_response = apigw.create_api(
            Name=API_NAME,
            ProtocolType='HTTP',
            Target=lambda_arn
        )
        api_id = api_response['ApiId']
        api_endpoint = api_response['ApiEndpoint']
        
        # Fetch the 12-digit AWS Account ID dynamically
        account_id = sts.get_caller_identity()['Account']
        
        # Grant API Gateway permission to execute our Lambda function
        print("Granting execution permissions...")
        try:
            lam.add_permission(
                FunctionName=LAMBDA_NAME,
                StatementId='apigateway-invoke-permissions',
                Action='lambda:InvokeFunction',
                Principal='apigateway.amazonaws.com',
                SourceArn=f"arn:aws:execute-api:{REGION}:{account_id}:{api_id}/*/*"
            )
        except lam.exceptions.ResourceConflictException:
            pass # Permission already exists

        print("\n Your Serverless API is live.")
        print(f"Click this link to test it: {api_endpoint}")
        
    except Exception as e:
        print(f"Error creating API Gateway: {e}")

if __name__ == "__main__":
    create_public_endpoint()