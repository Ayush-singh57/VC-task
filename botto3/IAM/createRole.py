import boto3
import json

ROLE_NAME = "boto3-ec2-access-role"
POLICY_ARN = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"

def create_iam_role():
    iam = boto3.client('iam')
    trust_policy = {
        "Version": "2012-10-17",
        "Statement": [{"Effect": "Allow", "Principal": {"Service": "ec2.amazonaws.com"}, "Action": "sts:AssumeRole"}]
    }
    
    try:
        iam.create_role(RoleName=ROLE_NAME, AssumeRolePolicyDocument=json.dumps(trust_policy))
        iam.attach_role_policy(RoleName=ROLE_NAME, PolicyArn=POLICY_ARN)
        print(f" Success: Role '{ROLE_NAME}' created and policy attached.")
        
    except iam.exceptions.EntityAlreadyExistsException:
        print(f" Role '{ROLE_NAME}' already exists.")
    except Exception as e:
        print(f" Error: {e}")

if __name__ == "__main__":
    create_iam_role()