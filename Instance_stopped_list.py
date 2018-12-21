import boto3
client=boto3.client('ec2','ap-south-1')

resp = client.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': ['stopped']
        }

      ]
   )

for reservation in resp['Reservations']:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            print(f'Instance id in {instance_id} ')

