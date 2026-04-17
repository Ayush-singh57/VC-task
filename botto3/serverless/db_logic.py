import boto3
import os
import uuid

db = boto3.client('dynamodb')

def save_user_visit(name):
   
    table = os.environ.get('DB_TABLE_NAME')
    unique_id = str(uuid.uuid4())[:8]
    
    try:
        db.put_item(
            TableName=table,
            Item={
                'id': {'S': unique_id},
                'UserName': {'S': name},
                'Timestamp': {'S': '2023-10-27'} # Example date
            }
        )
        print(f"Saved record for {name} to {table}")
        return True
    except Exception as e:
        print(f"Error saving to DB: {e}")
        return False