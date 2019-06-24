want_to_go_places = ['Manchester', 'East Coker', 'Paris', 'Rome', 'Berlin', 'Singapore', 'Beijing']

print(want_to_go_places)
print(f"Hey here's that list temporarily reversed : {sorted(want_to_go_places)}\nAnd here it is again in the original order : {want_to_go_places}")
want_to_go_places.reverse()
print(f"Here it is actually reversed:\n{want_to_go_places}")
want_to_go_places.reverse()
print(f"And here it is reversed back the way it was: \n{want_to_go_places}")
want_to_go_places.sort()
print(f"Here's the sorted list:\n{want_to_go_places}")
want_to_go_places.sort(reverse=True)
print(f"Here's the list sorted in reverse with the .sort method:\n{want_to_go_places}")

print(f"There are {len(want_to_go_places)} places that I want to go.")