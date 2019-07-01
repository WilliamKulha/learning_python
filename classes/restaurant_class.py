class Restaurant :
  """ A naive attempt to model a restaurant"""

  def __init__(self, restaurant_name, cuisine_type, seating_capacity) :
    """Initialize attributes to describe the restaurant"""
    self.name = restaurant_name
    self.cuisine_type = cuisine_type
    self.capacity = seating_capacity
  
  def describe_restaurant(self) :
    print(f"This restaurant is called {self.name}. It serves {self.cuisine_type}, and has a seating capacity of {self.capacity}.")
  
  def open_restaurant(self) :
    print(f"{self.name} is now open for business!")

nan_ban_tei = Restaurant('Nanbantei', 'Hokkaido Comfort Food', 56)

nan_ban_tei.describe_restaurant()

nan_ban_tei.open_restaurant()

tsujiya = Restaurant("Tsujiya's Soup Curry", "Soup Curry", 25)

tsujiya.describe_restaurant()

mori_no_horu = Restaurant("Mori No Horu", "Local Doto Delicacies", 18)

mori_no_horu.describe_restaurant()

class IceCreamStand(Restaurant) :
  """A Naive subclass of the Restaurant class"""
  def __init__(self, restaurant_name, cuisine_type, seating_capacity, flavors) :
    super().__init__(restaurant_name, cuisine_type, seating_capacity)
    self.flavors = flavors
  
  def list_flavors(self) :
    print(f"Here are the flavors available at {self.name}")
    for flavor in self.flavors :
      print(f"{flavor}")
  

michi_no_eki = IceCreamStand('Michi No Eki', "Ice Cream", 10, ['Orange', 'Vanilla', 'Chocolate', 'Strawberry', 'Sakura Mochi', 'Maccha', 'Kurumi'])

michi_no_eki.describe_restaurant()
michi_no_eki.list_flavors()