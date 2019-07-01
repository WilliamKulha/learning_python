"""A module to describe admin priveleges as a class"""

class Priveleges :
  """A naive representation of priveleges as a class."""
  def __init__(self, priveleges) :
    self.priveleges = priveleges

  def display_priveleges(self) :
    """ Method to list all the priveleges of the admin user."""
    print(f"This administrator has the following priveleges:")
    for privelege in self.priveleges :
      print(f"{privelege}")

