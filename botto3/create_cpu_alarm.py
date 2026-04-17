import boto3

def setup_cpu_monitoring(instance_id):
    cloudwatch = boto3.client('cloudwatch')
    
    print(f" Configuring CloudWatch CPU Alarm for Instance: {instance_id}")
    
    try:
        # Create or update the alarm
        cloudwatch.put_metric_alarm(
            AlarmName=f'High-CPU-Alert-{instance_id}',
            AlarmDescription='Triggers if CPU exceeds 80% for 5 consecutive minutes',
            ActionsEnabled=False, # Set to True if you add an SNS Topic ARN to send emails
            MetricName='CPUUtilization',
            Namespace='AWS/EC2',
            Statistic='Average',
            
            # The specific server to watch
            Dimensions=[
                {
                    'Name': 'InstanceId',
                    'Value': instance_id
                },
            ],
            
            # The Evaluation Logic
            Period=300,            # 300 seconds = 5 minutes per data point
            EvaluationPeriods=1,   # Number of periods it must be high to trigger ALARM
            Threshold=80.0,        # The 80% CPU limit
            ComparisonOperator='GreaterThanThreshold'
        )
        print("CloudWatch Alarm successfully created!")
        
    except Exception as e:
        print(f"Error creating alarm: {e}")

if __name__ == "__main__":
    setup_cpu_monitoring('i-04d9826396dd53221')