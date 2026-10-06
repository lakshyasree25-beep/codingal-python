print("Stars")

rows = int(input("Rows: "))

for i in range(rows):
for j in range(i + 1):
print("*", end=" ")
print()

print("Numbers")

rows = int(input("Rows: "))

number = 1

for i in range(rows):
for j in range(i + 1):
print(number, end=" ")
number = number + 1
print()

print("Diamond")

rows = int(input("Rows: "))

for i in range(rows):
for j in range(rows - i):
print(" ", end="")

for j in range(i + 1):
    print(j + 1, end=" ")

print("Done")
