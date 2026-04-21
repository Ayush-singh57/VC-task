import boto3
import json
from datetime import datetime
 
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super(DateTimeEncoder, self).default(obj)

def extract_lambda_inventory(output_filename='lambda_inventory.json'):
    # Initialize the Boto3 Lambda client
    lambda_client = boto3.client('lambda')
    
    # Use a Paginator in case you have more than 50 functions in your account!
    paginator = lambda_client.get_paginator('list_functions')
    
    extracted_data = {"lambda_functions": []}
    
    print("🔍 Scanning AWS account for Lambda functions...")
    print("-" * 50)

    try:
        # Loop through pages of results
        for page in paginator.paginate():
            for func in page['Functions']:
                
            
                clean_function_data = {
                    "FunctionName": func.get('FunctionName'),
                    "Runtime": func.get('Runtime', 'N/A'),
                    "MemorySizeMB": func.get('MemorySize'),
                    "TimeoutSeconds": func.get('Timeout'),
                    "LastModified": func.get('LastModified')
                }
                
                extracted_data["lambda_functions"].append(clean_function_data)
                print(f"   ↳ Found: {clean_function_data['FunctionName']} ({clean_function_data['Runtime']})")
                
        # 3. Write the extracted data to a clean local JSON file
        with open(output_filename, 'w') as json_file:
            json.dump(extracted_data, json_file, indent=4, cls=DateTimeEncoder)
            
        print("-" * 50)
        print(f" Extracted {len(extracted_data['lambda_functions'])} functions.")
        print(f"Saved to: {output_filename}")

    except Exception as e:
        print(f"Error fetching Lambda functions: {e}")

if __name__ == "__main__":
    extract_lambda_inventory()