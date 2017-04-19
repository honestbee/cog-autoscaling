from cog.command import Command

class AutoscalingBase(Command):
  def __init__(self):
    super().__init__()
    self.access_key_id = None
    self.secret_access_key = None

  def prepare(self):
    self.access_key_id = self.config("access_key_id")
    if self.access_key_id == None:
      self.fail("Missing dynamic configuration variable 'access_key_id'.")

    self.secret_access_key = self.config("secret_access_key")
    if self.secret_access_key == None:
      self.fail("Missing dynamic configuration variable 'secret_access_key'.")
