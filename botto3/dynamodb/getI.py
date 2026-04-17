import boto3

TABLE_NAME = "task-table-boto3"

def read_item():
    table = boto3.resource('dynamodb', region_name='ap-south-1').Table(TABLE_NAME)
    
    try:
        
        response = table.get_item(Key={'UserId': 'user_123'})
        
        if 'Item' in response:
            print(f" Found User Data:\n{response['Item']}")
        else:
            print(" Item not found in the database.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    read_item()