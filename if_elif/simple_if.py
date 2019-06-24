foods = ['cookies', 'beans', 'brownies', 'eggplant', 'tempura', 'sushi', 'water chestnuts']
favorite = 'cookies'
hated = 'water chestnuts'

for food in foods:
  if food == favorite :
    print(food.upper())
  else:
    print(food.title())
  
for food in foods :
  if food != hated:
    print(food)

print('beans' in foods)