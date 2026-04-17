import boto3

# 1. Connect to EC2 in your preferred region
ec2 = boto3.client('ec2', region_name='ap-south-1')

def check_my_servers():
    
    print(" Scanning for EC2 instances...")
    
    try:
        #describe_instances
        response = ec2.describe_instances()
        
        count = 0
        for reservation in response.get('Reservations', []):
            for instance in reservation.get('Instances', []):
                count += 1
                instance_id = instance['InstanceId']
                state = instance['State']['Name']
              
                name = "Unnamed"
                for tag in instance.get('Tags', []):
                    if tag['Key'] == 'Name':
                        name = tag['Value']
                
                print(f" - [{name}] ID: {instance_id} | State: {state}")
        
        if count == 0:
            print(" No instances found in this region.")
            
    except Exception as e:
        print(f" Error: {e}")

if __name__ == "__main__":
    check_my_servers()