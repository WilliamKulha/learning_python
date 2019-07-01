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
  

jeff_d = User("Jeff", "Dorowicz", 22, "Richmond", "Painter")

jeff_d.print_self()

jeff_d.greet_user()