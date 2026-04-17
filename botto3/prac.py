import boto3
from pprint import pprint

aws_management_console = boto3.session.Session(profile_name = 'default')

iam_console = aws_management_console.client(service_name = 'iam')

result = iam_console.list_users()
for each_user in result['Users']:
    print(each_user['UserName'])