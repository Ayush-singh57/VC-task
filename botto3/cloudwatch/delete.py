import boto3

REGION = 'ap-south-1'

def cleanup_monitoring():
    sns = boto3.client('sns', region_name=REGION)
    cw = boto3.client('cloudwatch', region_name=REGION)

    try:
        # 1. Delete the CloudWatch Alarm
        cw.delete_alarms(AlarmNames=['High-CPU-Utilization'])
        print("CloudWatch alarm deleted.")

        # 2. Find and delete the SNS Topic
        topics_response = sns.list_topics()
        for topic in topics_response.get('Topics', []):
            topic_arn = topic['TopicArn']
            if 'EC2-Critical-Alerts' in topic_arn:
                sns.delete_topic(TopicArn=topic_arn)
                print(f" SNS Topic deleted. ARN: {topic_arn}")
                break
                
    except Exception as e:
        print(f"Error during cleanup: {e}")

if __name__ == "__main__":
    cleanup_monitoring()