import boto3

def launch_test_instance():
    ec2 = boto3.client('ec2')
    
    print(" Launching EC2 Instance for CPU Test")
    
    user_data_script = '''#!/bin/bash
    dnf update -y
    dnf install stress -y
    '''
    
    try:
        response = ec2.run_instances(
            ImageId='resolve:ssm:/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64',
            InstanceType='t3.micro', # Free-tier eligible
            MinCount=1,
            MaxCount=1,
            UserData=user_data_script,
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [{'Key': 'Name', 'Value': 'CPU-Chaos-Test'}]
                }
            ]
        )
        
        instance_id = response['Instances'][0]['InstanceId']
        print(f" Instance launched successfully!")
        print(f"Copy this Instance ID: {instance_id}")
        print("Wait some few mintues ")
        
    except Exception as e:
        print(f"Error launching instance: {e}")

if __name__ == "__main__":
    launch_test_instance()