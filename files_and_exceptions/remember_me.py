import json

# Load the username if it's been saved
# Otherwise ask for the name and save it.
def get_stored_username() :
  """Get stored username if it's available"""
  filename = 'username.json'
  try :
    with open(filename) as f :
      username = json.load(f)
  except FileNotFoundError :
    return None
  else :
    return username

def get_new_username() :
  """Prompt for and save a new username"""
  username = input("What's your name?\n")
  filename = 'username.json'
  with open(filename, 'w') as f :
    json.dump(username, f)
  return username


def greet_user() :
  """Greet the user by name"""
  username = get_stored_username()
  if username :
    same_user = input(f"Hey, is that you, {username}?\n enter y if it is and n if it isn't\n")
    if same_user == 'y' :
      print(f"Hey, welcome back {username}!")
    else :
     get_new_username()
  else :
    get_new_username()
    print(f"We'll remember you when you come back, {username}!")

greet_user()