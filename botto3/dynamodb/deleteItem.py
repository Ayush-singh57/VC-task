import boto3

TABLE_NAME = "boto3-portfolio-table"

def delete_item():
    table = boto3.resource('dynamodb', region_name='ap-south-1').Table(TABLE_NAME)
    
    try:
        table.delete_item(Key={'UserId': 'user_123'})
        print(" Item permanently deleted from DynamoDB.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    delete_item()