import boto3
import yaml
from botocore.exceptions import ClientError

def load_yaml_config(filepath):
    """Reads the YAML file and returns the parsed dictionary."""
    with open(filepath, 'r') as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(f"Error parsing YAML file: {exc}")
            return None

def manage_iam_users(config_file):
    # Initialize the Boto3 IAM client
    iam_client = boto3.client('iam')
    config = load_yaml_config(config_file)
    
    if not config or 'users' not in config:
        print("Invalid YAML format or empty file.")
        return

    print("🚀 Starting IAM User Automation...")
    print("-" * 40)

    for user_data in config['users']:
        username = user_data['username']
        groups = user_data.get('groups', [])

        # 1. Create the IAM User
        try:
            iam_client.create_user(UserName=username)
            print(f"✅ Created User: {username}")
        except ClientError as e:
            if e.response['Error']['Code'] == 'EntityAlreadyExists':
                print(f"⚠️  User already exists: {username} (Skipping creation)")
            else:
                print(f"❌ Error creating user {username}: {e}")
                continue

        # 2. Assign User to Groups (With Auto-Creation)
        for group in groups:
            try:
                # Try to add the user to the group
                iam_client.add_user_to_group(GroupName=group, UserName=username)
                print(f"   ↳ Added to existing group: {group}")
            except ClientError as e:
                # If the group doesn't exist, create it first!
                if e.response['Error']['Code'] == 'NoSuchEntity':
                    print(f"   ⚠️ Group '{group}' not found. Creating it now...")
                    try:
                        iam_client.create_group(GroupName=group)
                        iam_client.add_user_to_group(GroupName=group, UserName=username)
                        print(f"   ↳ ✅ Created group '{group}' and added user.")
                    except ClientError as create_err:
                        print(f"   ❌ Error creating group '{group}': {create_err}")
                else:
                    print(f"   ❌ Error adding {username} to {group}: {e}")
                    
    print("-" * 40)
    print("🏁 Automation Complete!")

if __name__ == "__main__":
  manage_iam_users('iam_users.yaml')