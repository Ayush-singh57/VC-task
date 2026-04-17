import boto3

TABLE_NAME = "task-table-boto3"

def delete_table():
    table = boto3.resource('dynamodb', region_name='ap-south-1').Table(TABLE_NAME)
    
    try:
        table.delete()
        print(f"Deleting table '{TABLE_NAME}'...")
        table.wait_until_not_exists() 
        print(" Table has been deleted ")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    delete_table()