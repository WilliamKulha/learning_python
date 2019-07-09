cats = 'cats.txt'
dogs = 'dogs.txt'

def read_animal_names_file(file_to_open) :
  """Read a list of animal names from a txt file separated by new lines"""
  try:
    with open(file_to_open, 'r') as f:
      animal_names = f.read()
      print(f"Here are the names of the {file_to_open}:\n")
      print(animal_names)
  except FileNotFoundError :
    pass

read_animal_names_file(cats)
read_animal_names_file(dogs)