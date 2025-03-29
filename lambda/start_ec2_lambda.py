import boto3


def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    instance_id = "i-0123456789abcdef0"  # Replace with actual EC2 instance ID

    try:
        response = ec2.start_instances(InstanceIds=[instance_id])
        print(f"Started instance {instance_id}, Response: {response}")
        return {
            'statusCode': 200,
            'body': f'Instance {instance_id} started successfully.'
        }
    except Exception as e:
        print(f"Error starting instance: {str(e)}")
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
