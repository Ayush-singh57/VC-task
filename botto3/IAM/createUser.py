import boto3

USER_NAME = "boto3-portfolio-user"
POLICY_ARN = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"

def create_iam_user():
    iam = boto3.client('iam')
    
    try:
        iam.create_user(UserName=USER_NAME)
        iam.attach_user_policy(UserName=USER_NAME, PolicyArn=POLICY_ARN)
        print(f"done: User '{USER_NAME}' created and policy attached.")
        
    except iam.exceptions.EntityAlreadyExistsException:
        print(f" User '{USER_NAME}' already exists.")
    except Exception as e:
        print(f" Error: {e}")

if __name__ == "__main__":
    create_iam_user()