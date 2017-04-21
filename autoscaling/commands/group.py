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

  def describe_groups(self):
    return self.client.describe_auto_scaling_groups()

  def get_group_name_by_tag(self):
    for group in self.describe_groups():
      for tag in g['Tags']:
        if tag['Key'] == "elasticbeanstalk:environment-name" and tag['Value'] == self.request.options['tag']:
          name = group['AutoScalingGroupName']
          break

    return name

  def list(self):
    for group in self.describe_groups():
      print(group['AutoScalingGroupName'])

  def scale(self):
    if self.request.options['name']:
      name = self.request.options['name']
    elif self.request.options['tag']:
      name = self.get_group_name_by_tag()
    else:
      self.fail("Tag or name unknown or not provided")

    response = self.client.set_desired_capacity(
      AutoScalingGroupName = name,
      DesiredCapacity = int(self.request.options['desired']),
      HonorCooldown = False
    )

    print("Set %s capacity to %s instances" % (self.request.options['name'], self.request.options['desired']))

  def parse_subcommand_(self):
    if self.request.args == None:
      return self.list
    if self.request.args[0] == "list":
      return self.list
    if self.request.args[0] == "scale":
      return self.scale
    self.fail("Unknown subcommand: '%s'" % self.request.args[0])
