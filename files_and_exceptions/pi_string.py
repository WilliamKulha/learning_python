filename = 'pi_digits.txt'

with open(filename) as my_file :
  lines = my_file.readlines()

pi_string = ''
for line in lines :
  pi_string += line.strip()

print(pi_string)
print(len(pi_string))