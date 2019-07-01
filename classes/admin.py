"""A module to naively represent the admin subclass of users."""

from user import User
from privelege import Priveleges

class Admin(User) :
  """A naive attempt to add an administrator subclass to the User class"""
  def __init__(self, first_name, last_name, age, location, profession, priveleges) :
    """Initialize attributes of the parent class"""
    super().__init__(first_name, last_name, age, location, profession)
    self.priveleges = Priveleges(priveleges)
    