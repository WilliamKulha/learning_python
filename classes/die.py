"""A module to naively describe dice as an object"""
from random import randint

class Die :
  """A naive attempt to model die as a python object"""
  def __init__(self) :
    """Initialize die with a default of 6 sides"""
    self.sides = 6
  
  def roll_die(self) :
    outcome = randint(1, self.sides)
    print('Rolling die...')
    print('...')
    print(outcome)
  
  def roll_ten_times(self) :
    count = 0
    while count <= 10 :
      self.roll_die()
      count += 1


my_die = Die()
my_die.roll_ten_times()

my_die_2 = Die()
my_die_2.sides = 10
my_die_2.roll_ten_times()

my_die_3 = Die()
my_die_3.sides = 20
my_die_3.roll_ten_times()



