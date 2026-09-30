# Homework Tracker

total = 4
completed = 0

print("You have 4 homework tasks today!")

while completed < total:

    if completed == 0:
        task = "Math worksheet"
    elif completed == 1:
        task = "Science reading"
    elif completed == 2:
        task = "English writing"
    else:
        task = "Coding practice"

    answer = input("Did you finish " + task + "? (yes/no): ")

    if answer == "yes":
        completed += 1
        print("Good job!")
    else:
        print("Keep working!")

    print("Homework left:", total - completed)
    print()

print("All homework is complete!")
print("Great job!")

print("\nHomework Summary")
print("Assigned:", total)
print("Completed:", completed)
print("Remaining:", total - completed)