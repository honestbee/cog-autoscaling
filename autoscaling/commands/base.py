from cog.command import Command

class AutoscalingBase(Command):
  def __init__(self):
    super().__init__()
    self.aws_access_key_id = None
    self.aws_secret_access_key = None
    self.aws_default_region = None

  def prepare(self):
    self.aws_access_key_id = self.config("aws_access_key_id")
    if self.aws_access_key_id == None:
      self.fail("Missing dynamic configuration variable 'aws_access_key_id'.")

    self.aws_secret_access_key = self.config("aws_secret_access_key")
    if self.aws_secret_access_key == None:
      self.fail("Missing dynamic configuration variable 'aws_secret_access_key'.")

    self.region = self.config("region")
    if self.region == None:
      self.fail("Missing dynamic configuration variable 'region'.")
