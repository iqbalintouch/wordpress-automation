import boto3
import json


def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Replace with your EC2 instance ID
    instance_id = 'i-xxxxxxxxxxxxxxxxx'

    try:
        response = ec2.start_instances(InstanceIds=[instance_id])
        print(f"Instance {instance_id} has been started successfully.")
        return {
            'statusCode': 200,
            'body': json.dumps(f'Instance {instance_id} started successfully')
        }
    except Exception as e:
        print(f"Error starting instance {instance_id}: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error starting instance {instance_id}: {str(e)}')
        }
