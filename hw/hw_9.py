import keyword

# Get information
name = input("Name: ")
goal = input("Goal: ")
month = input("Target month: ")

minutes = 30

# Show goal plan
print("\n--- PERSONAL GOAL ---")
print("Name:", name)
print("Goal:", goal)
print("Month:", month)
print("Practice:", minutes, "minutes a day")

print("\nStatus: Not Started")

print("\n" + name, "will practice", goal, "for", minutes, "minutes each day.")