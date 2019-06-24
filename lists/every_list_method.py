languages = ['English', 'Japanese', 'Italian', 'Spanish', 'German', 'Swedish', 'Icelandic', 'Portugeuse', 'Arabic']
print(f"The 2nd language in the list is {languages[1]}.")

languages.append('Mandarin')
print(languages)

languages.insert(4, 'Dutch')
print(languages)

popped = languages.pop(5)
print(popped)

languages.remove('Japanese')
print(languages)

languages.sort()

print(f"This is everything sorted:\n{languages}")


print(f"The first three languages are:{languages[:3]}")

print(f"Three items from the middle of the list are: {languages[3:6]}")

print(f"Three items from the end of the list are {languages[-3:]}")
