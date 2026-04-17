import boto3

INSTANCE_ID = "i-0840857fe2a50e433"
ec2 = boto3.client('ec2', region_name='ap-south-1')

def delete_server_forever():
    print(f" Terminating instance: {INSTANCE_ID}")
    
    try:
        # terminate_instances
        ec2.terminate_instances(InstanceIds=[INSTANCE_ID])
        print("The instance has been scheduled for termination.")
        
    except Exception as e:
        print(f" Termination failed: {e}")

if __name__ == "__main__":
    delete_server_forever()