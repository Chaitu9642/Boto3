import boto3
client=boto3.client('ec2')
client.stop_instances( InstanceIds=['i-0628f8a17ea405114'] )