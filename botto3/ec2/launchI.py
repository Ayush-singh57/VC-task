import boto3

# Configuration
REGION = 'ap-south-1'

# use two services now: SSM (to find the AMI) and EC2 (to launch the server)
ssm_client = boto3.client('ssm', region_name=REGION)
ec2 = boto3.resource('ec2', region_name=REGION)

def get_latest_ami():
 
    response = ssm_client.get_parameter(
        Name='/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64'
    )
    return response['Parameter']['Value']

def launch_new_server():
   
    
    try:
 
        dynamic_ami_id = get_latest_ami()
        
        
        print(f" Launching a new t3.micro server : {dynamic_ami_id}...")
        
       
        instances = ec2.create_instances(
            ImageId=dynamic_ami_id,
            InstanceType='t3.micro', 
            MinCount=1,
            MaxCount=1,
            TagSpecifications=[{
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'Name', 'Value': 'My-Boto3-Lab-Server'},
                    {'Key': 'Environment', 'Value': 'Dev'}
                ]
            }]
        )
        
        new_instance = instances[0]
        print(f"Success! New instance created with : {new_instance.id}")
        print("Wait a few minutes for 'running' state.")
        
    except Exception as e:
        print(f"Launch failed: {e}")

if __name__ == "__main__":
    launch_new_server()