import boto3

def deploy_flask_to_ecs():
    ecs_client = boto3.client('ecs')
    
    # --- CONFIGURATION ---
    CLUSTER_NAME = "flask-cluster" 
    IMAGE_URI = "835637956758.dkr.ecr.ap-south-1.amazonaws.com/ecs-ec2:latest"
    TARGET_GROUP_ARN = "arn:aws:elasticloadbalancing:ap-south-1:835637956758:targetgroup/falsk-tg/02cd2d70b77d185c"
     
    print(" Starting  Flask ECS Deployment...")

    try:
        task_response = ecs_client.register_task_definition(
            family='flask-app-task',
            requiresCompatibilities=['EC2'],
            networkMode='bridge',
            containerDefinitions=[{
                'name': 'flask-container',
                'image': IMAGE_URI,
                'cpu': 256,
                'memory': 512,
                'essential': True,
                'portMappings': [{'containerPort': 5000, 'hostPort': 0, 'protocol': 'tcp'}]
            }]
        )
        task_def_arn = task_response['taskDefinition']['taskDefinitionArn']
        print(f"Blueprint created!")
    except Exception as e:
        print(f"Failed Blueprint: {e}"); return

    # Step 2: Create Service
    try:
        ecs_client.create_service(
            cluster=CLUSTER_NAME, 
            serviceName='flask-api-service',
            taskDefinition=task_def_arn,
            desiredCount=2,
            launchType='EC2',
            loadBalancers=[{'targetGroupArn': TARGET_GROUP_ARN, 'containerName': 'flask-container', 'containerPort': 5000}]
        )
        print("  AWS is deploying your containers.")
    except Exception as e:
        print(f"  Failed: {e}")

if __name__ == "__main__":
    deploy_flask_to_ecs()