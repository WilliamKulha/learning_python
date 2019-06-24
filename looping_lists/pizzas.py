pizzas = ['Margherita', 'Sicilian', 'Neopolitan']

for pizza in pizzas:
  print(pizza)

for pizza in pizzas:
  print(f"Oh my god! Have you tried their {pizza} pizza?? It's to die for!\n")

print("\nMan I really love pizza!")

friends_pizzas = pizzas[:]

pizzas.insert(0, 'Meat Lovers')

friends_pizzas.insert(0, 'Supreme')

print(f"Here's the original list: {pizzas}\nHere's the friends list:{friends_pizzas}")

print("My favorite pizzas are:")
for pizza in pizzas:
  print(pizza)
  