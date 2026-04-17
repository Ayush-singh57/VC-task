import boto3

session = boto3.Session()
credentials = session.get_credentials()

print("Access Key being used:", credentials.access_key)
print("Region from session:", session.region_name)
