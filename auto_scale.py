## Auto scale DAF Shopping cart intrastructure
## creating change request in Freshservice
## date - 10 / 08 / 2023


import boto3

client = boto3.client('autoscaling')
response = client.attach_instances(
    InstanceIds=[
        'AWS_EC1','AWS_EC2'
    ],
    AutoScalingGroupName='core_instances'
)

response = client.set_desired_capacity(
    AutoScalingGroupName='core_instances',
    DesiredCapacity=255,
    HonorCooldown=True
)
