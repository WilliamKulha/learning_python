class Dog :
    """A simple attempt to model a dog"""

    def __init__(self, name, age) :
      """Initialize name and age attributes"""
      self.name = name
      self.age = age

    def sit(self) :
      """Simulate a dog sitting when commanded to"""
      print(f"{self.name} is now sitting.")
    
    def roll_over(self) :
      """Simulate a dog rolling over when commanded to"""
      print(f"{self.name} rolled over!!")

my_favorite_dog = Dog('Bree', 12)

print(f"My favorite old dog was called {my_favorite_dog.name}")
print(f"Sadly, she died when she was {my_favorite_dog.age}")

my_favorite_dog.roll_over()
my_favorite_dog.sit()

my_parents_old_dog = Dog('Tilly', 14)

print(f"\nMy parent's old dog is called {my_parents_old_dog.name}")
print(f"She's actually {my_parents_old_dog.age} years old and still kicking!")

my_parents_old_dog.roll_over()
my_parents_old_dog.sit()


