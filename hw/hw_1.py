def bill(a, b):
tip = a * b / 100
total = a + tip
print("Total:", total)
return total

bill(150, 20)

def seats(n):
"""Finds seating arrangements."""

if n <= 1:
    return 1
else:
    return n * seats(n - 1)

print(seats.**doc**)

print("1 guest:", seats(1))
print("2 guests:", seats(2))
print("3 guests:", seats(3))
print("5 guests:", seats(5))