import boto3

def asg_client():
  client = boto3.client('autoscaling')
  return client
