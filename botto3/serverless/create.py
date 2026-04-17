import json

def lambda_handler(event, context):
    print(" Lambda has been triggered!")
    
    name = event.get('name', 'World')
    
    message = f"Hello, {name}! This is my first serverless function."
    
    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }