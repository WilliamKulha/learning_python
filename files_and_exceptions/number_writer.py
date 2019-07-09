import json

numbers = [1, 29, 2, 5, 23, 6, 24, 15, 11, 10, 19]

filename = 'numbers.json'
with open(filename, 'w') as f:
  json.dump(numbers, f)
