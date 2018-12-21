import boto3

client = boto3.client('ec2')
client.stop_instances(
    InstanceIds=['i-09ecd3854464dab09']
)
