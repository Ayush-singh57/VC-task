import boto3

INSTANCE_ID = "i-0840857fe2a50e433" 

ec2 = boto3.client('ec2', region_name='ap-south-1')

def stop_server():
  
    print(f" Attempting to stop instance: {INSTANCE_ID}")
    
    try:
        ec2.stop_instances(InstanceIds=[INSTANCE_ID])
        print(" great instance stop!")
        
    except Exception as e:
        print(f" Failed to stop: {e}")

if __name__ == "__main__":
    stop_server()