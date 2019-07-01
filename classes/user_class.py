class Priveleges :
  """A class to represent priveleges"""
  def __init__(self, priveleges) :
    """Initialize the list of priveleges"""
    self.priveleges = priveleges

  def display_priveleges(self) :
    """ Method to list all the priveleges of the admin user."""
    print(f"This administrator has the following priveleges:")
    for privelege in self.priveleges :
      print(f"{privelege}")


class User :
  """A naive attempt to model a user object"""
  def __init__(self, first_name, last_name, age, location, profession) :
    self.first_name= first_name
    self.last_name = last_name
    self.age = age
    self.location = location
    self.profession = profession

  def print_self(self) :
    """Print out all the information that the user object contains with a label """
    print(f"User Name : {self.first_name} {self.last_name}")
    print(f"Age : {self.age}")
    print(f"Location : {self.location}")
    print(f"Profession : {self.profession}")
  
  def greet_user(self) :
    """Greet the user by their first name. """
    print(f"\nWell hey there {self.first_name}! How're you today?")

class Admin(User) :
    """A naive attempt to add an administrator subclass to the User class"""
    def __init__(self, first_name, last_name, age, location, profession, priveleges) :
      """Initialize attributes of the parent class"""
      super().__init__(first_name, last_name, age, location, profession)
      self.priveleges = Priveleges(priveleges)
    
admin_jake = Admin(
    'Jake', 'Rubberneck', 33, 'Johannesburg', 'Electrician', ['Approve posts', 'Reject posts', 'Ban users'])

admin_jake.priveleges.display_priveleges()

