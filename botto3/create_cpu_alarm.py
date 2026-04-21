import boto3

def setup_cpu_monitoring(instance_id):
    cloudwatch = boto3.client('cloudwatch')
    
    print(f" Configuring CloudWatch CPU Alarm for Instance: {instance_id}")
    
    try:
        cloudwatch.put_metric_alarm(
            AlarmName=f'High-CPU-Alert-{instance_id}',
            AlarmDescription='Triggers if CPU exceeds 80% for 5 consecutive minutes',
            ActionsEnabled=False,  
            MetricName='CPUUtilization',
            Namespace='AWS/EC2',
            Statistic='Average',
            
            Dimensions=[
                {
                    'Name': 'InstanceId',
                    'Value': instance_id
                },
            ],
            
            Period=300,             
            EvaluationPeriods=1,   
            Threshold=80.0,         
            ComparisonOperator='GreaterThanThreshold'
        )
        print("CloudWatch Alarm successfully created!")
        
    except Exception as e:
        print(f"Error creating alarm: {e}")

if __name__ == "__main__":
    setup_cpu_monitoring('i-04d9826396dd53221')