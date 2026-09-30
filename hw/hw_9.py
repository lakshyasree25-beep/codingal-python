name = input("What is your name? ")
club = input("What is your club? ")

number = 8
points = 9.5
events = 6
active = True

print("Name:", name)
print("Club:", club)
print("Number:", number)
print("Points:", points)
print("Events:", events)
print("Active:", active)

number = str(number)
points = str(points)
events = str(events)

print("Number as text:", number)
print("Points as text:", points)
print("Events as text:", events)

badge = name[:3] + name[-1]

print("Badge:", badge)

reverse = club[::-1]

print("Club backwards:", reverse)

print("===== CLUB BADGE =====")
print("Name:", name)
print("Badge:", badge)
print("ID:", number)
print("Points:", points)
print("Events:", events)
print("Active:", active)
print("Club Code:", reverse)