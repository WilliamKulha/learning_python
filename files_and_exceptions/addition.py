def add_two_digits(num1, num2) :
    """Add two numbers"""
    try :
      num1  = int(num1)
      num2 = int(num2)
    except ValueError :
      print("Hey, one of those isn't a number!")
    else :
      result = num1 + num2
      print(f"The result is: {result}")
          

print("enter 'q' to quit at anytime.")
print("Please enter two numbers")

while True :
  num1 = input("Enter the first number ")
  if (num1  == 'q'):
    break
  else :
    num2 = input("Enter the second number ")
    if (num2 == 'q') :
      break
    else :
      print(f"Number one is {num1}")
      print(f"Number two is {num2}")

      add_two_digits(num1, num2)


