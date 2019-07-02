filename = 'guest_book.txt'

print("Enter 'quit' when you're finished!")
while True :
  name = input("\nWhat's your name?  ")
  if name == 'quit' :
    break
  else : 
    with open(filename, 'a') as open_file :
      open_file.write(name + "\n")
    print("Hi " + name + ", you've been added to the guest book!")