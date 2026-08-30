name = input("What is your name? ")
club = input("What club are you in? ")

member_id = 8
score = 9.5
event_total = 6
is_active = True

badge = name[0] + name[-1]
club_code = club[0:3]

print("Name:", name)
print("Club:", club)
print("ID:", member_id)
print("Score:", score)
print("Events:", event_total)
print("Active:", is_active)
print("Badge:",