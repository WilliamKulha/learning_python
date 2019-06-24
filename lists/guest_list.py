guest_list = ['George Martin', 'Oscar Wilde', 'Kurt Vonnegut', 'Carl Sagan', 'John Williams', 'William Shakespeare']
for guest in guest_list :
  print(f"\tDear {guest},\nYou are cordially invited to dinner with William Kulha.")

no_show = guest_list.pop(1)
print(f"{no_show} couldn't make it to dinner")
guest_list.insert(1, 'Dave Chapelle')
for guest in guest_list :
  print(f"\tDear {guest},\n\tYou are cordially invited to dinner with William Kulha")

print("\tHey everyone, I've just found a bigger table so we're going to have three more guests!")
guest_list.insert(0, 'Robin van Persie')
guest_list.insert(4, 'Sir Alex Ferguson')
guest_list.append('James Joyce')
for guest in guest_list :
  print(f"\tDear {guest},\n\tYou are cordially Invited to dinner with William Kulha et al.")

print('Sorry folks! Turns out the table will not arrive in time for the dinner. Only two people are going to be invited.')
popped = guest_list.pop(-1)
print(f"Sorry {popped}. You're no longer invited to dinner with William Kulha et al.")
popped = guest_list.pop(-2)
print(f"Sorry {popped}. You're no longer invited to dinner with William Kulha et al.")
popped = guest_list.pop(-2)
print(f"Sorry {popped}. You're no longer invited to dinner with William Kulha et al.")
popped = guest_list.pop(-2)
print(f"Sorry {popped}. You're no longer invited to dinner with William Kulha et al.")
popped = guest_list.pop(-3)
print(f"Sorry {popped}. You're no longer invited to dinner with William Kulha et al.")
popped = guest_list.pop(-3) 
print(f"Sorry {popped}. You're not invited to dinner anymore.")
popped = guest_list.pop(-3)
print(f"Sorry {popped}. You're not invited to dinner anymore.")
for guest in guest_list :
  print(f"Hey {guest}! I just wanted to let you know that you're still invited to dinner with William Kulha!")

del guest_list[0]
del guest_list[0]

print(guest_list)