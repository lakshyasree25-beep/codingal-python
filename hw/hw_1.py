name = input("Enter your name: ")
club = input("Enter your club name: ")

member_number = 8
points = 9.5
events = 6
hours = 1.5
active = True

print("Name:", name, type(name))
print("Club:", club, type(club))
print("Member Number:", member_number, type(member_number))

member_text = str(member_number)
events_text = str(events)
points_text = str(points)
active_text = str(active)

badge = name[:3] + name[-1]
secret_code = club[::-1]

print("")
print("===== CLUB BADGE =====")
print("MEMBER:", badge.upper())
print("ID:", member_text)
print("EVENTS:", events_text)
print("POINTS:", points_text)
print("ACTIVE:", active_text)
print("CODE:", secret_code.upper())
print("======================")