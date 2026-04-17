import boto3

TABLE_NAME = "task-table-boto3"

def update_item():
    table = boto3.resource('dynamodb', region_name='ap-south-1').Table(TABLE_NAME)
    
    try:
        table.update_item(
            Key={'UserId': 'user_123'},
            UpdateExpression="SET #r = :new_role",
            ExpressionAttributeNames={'#r': 'Role'},
            ExpressionAttributeValues={':new_role': 'Senior Cloud Engineer'}
        )
        print(" User Role has been updated.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_item()