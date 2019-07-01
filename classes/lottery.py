from random import randint
class LotteryCombos :
  """Class that holds the combos for a small lottery with 15 possible elements"""
  def __init__(self) :
    """Initialize the lottery combo with a tuple containing the possible elements"""
    self.lotto_elements = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'z', 'x', 'y', 'w', 'v')
  
  def pick_winner(self) :
    """Function to randomly select the four elements of the winning ticket"""
    winning_combo = []
    count = 0
    while count <= 3 :
      random = self.lotto_elements[randint(0, 14)]
      winning_combo.append(random)
      count += 1
    return winning_combo
  
my_test_lotto = LotteryCombos()

my_ticket = [5, 'v', 8, 'x']
print(my_ticket)
count = 0
pulled = my_test_lotto.pick_winner()
print(pulled)
while pulled != my_ticket :
  count += 1
  pulled = my_test_lotto.pick_winner()


print(f"For the ticket {my_ticket}, it took {count} drawings to win.")

