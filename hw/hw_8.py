print("Stars")

rows = int(input("Rows: "))

for i in range(rows):
for j in range(i + 1):
print("*", end=" ")
print()

print("Numbers")

rows = int(input("Rows: "))
num = 1

for i in range(rows):
for j in range(i + 1):
print(num, end=" ")
num = num + 1
print()

print("Diamond")

rows = int(input("Rows: "))

for i in range(rows):
print(" " * (rows - i), end="")

for j