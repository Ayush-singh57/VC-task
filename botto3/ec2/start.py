import boto3

INSTANCE_ID = "i-0840857fe2a50e433"
ec2 = boto3.client('ec2', region_name='ap-south-1')

def start_server():
  
    print(f" Attempting to start instance: {INSTANCE_ID}")
    
    try:
        ec2.start_instances(InstanceIds=[INSTANCE_ID])
        print(" gotcha server is running state now")
        
    except Exception as e:
        print(f" Failed to start: {e}")

if __name__ == "__main__":
    start_server()