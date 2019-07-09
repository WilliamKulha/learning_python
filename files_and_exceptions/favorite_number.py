import json

filename = 'favoriteNumber.json'

try :
  with open(filename) as f :
    favorite_number = json.load(f)
except FileNotFoundError :
  favorite_number = input("What's your favorite number?\n")
  with open(filename, 'w') as f :
    json.dump(favorite_number, f)
else : 
  print(f"Hey, I know your favorite number! It's {favorite_number}")

