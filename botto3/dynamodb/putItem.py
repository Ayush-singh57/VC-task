import boto3

TABLE_NAME = "task-table-boto3"

def add_item(): 
     
    # Connect directly to the specific table
    table = boto3.resource('dynamodb', region_name='ap-south-1').Table(TABLE_NAME)
    
    try:
        table.put_item(
            Item={
                'UserId': 'user_123', 
                'Name': 'Ayush', 
                'Role': 'Cloud Engineer'
            }
        )
        print(" Item added to DynamoDB.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    add_item()