import boto3

REGION = 'ap-south-1'
EMAIL_ADDRESS = "ayushchouhan401@gmail.com" 
INSTANCE_ID = "i-0840857fe2a50e433"     

def setup_monitoring():
    sns = boto3.client('sns', region_name=REGION)
    cw = boto3.client('cloudwatch', region_name=REGION)

    try:
        topic_response = sns.create_topic(Name='EC2-Critical-Alerts')
        topic_arn = topic_response['TopicArn']
        print(f"Success: SNS Topic created. ARN: {topic_arn}")
        
        # 2. Subscribe an email to the topic
        sns.subscribe(TopicArn=topic_arn, Protocol='email', Endpoint=EMAIL_ADDRESS)
        print(f"Subscribed {EMAIL_ADDRESS}. Please check your inbox to confirm.")

        # 3. Create the CloudWatch Alarm and link it to the SNS Topic
        cw.put_metric_alarm(
            AlarmName='High-CPU-Utilization',
            AlarmDescription='Triggers an email if CPU exceeds 80% for 5 minutes',
            ActionsEnabled=True,
            AlarmActions=[topic_arn],
            MetricName='CPUUtilization',
            Namespace='AWS/EC2',
            Statistic='Average',
            Dimensions=[{'Name': 'InstanceId', 'Value': INSTANCE_ID}],
            Period=300,
            EvaluationPeriods=1,
            Threshold=80.0,
            ComparisonOperator='GreaterThanThreshold'
        )
        print(f" CloudWatch alarm configured for instance {INSTANCE_ID}.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    setup_monitoring()