print("When everyone's entered their info, enter 'quit' to see the results!")
filename = "poll.txt"

while True:
  reason = input("Tell me why you like programming: ")
  if reason == 'quit' :
    break
  else :
    with open(filename, 'a+') as open_file :
      open_file.write(reason + "\n")

with open(filename, 'r') as open_file :
  results = open_file.read()
  print(results)
