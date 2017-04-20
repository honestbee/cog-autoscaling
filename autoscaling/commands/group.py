import boto3
from autoscaling.commands.base import AutoscalingBase

class Group(AutoscalingBase):
  def __init__(self):
    super().__init__()
    self.aws_access_key_id = None
    self.aws_secret_access_key = None
    self.aws_default_region = None
    self.client = boto3.client('autoscaling')

  def run(self):
    handler = self.parse_subcommand_()
    handler()

  def list(self):
    response = self.client.describe_auto_scaling_groups()
    for group in response['AutoscalingGroups']:
      print(group['AutoScalingGroupName'])

  def scale(self):
    response = self.client.set_desired_capacity(
      AutoScalingGroupName = self.request.options["name"],
      DesiredCapacity = self.request.options["desired"],
      HonorCooldown = False
    )
    
    print("Set %s capacity to %i instances" % (asg_name, desired_capacity))

  def parse_subcommand_(self):
    if self.request.args == None:
      return self.list
    if self.request.args[0] == "list":
      return self.list
    if self.request.args[0] == "scale":
      return self.scale
    self.fail("Unknown subcommand: '%s'" % self.request.args[0])
