# 1) Ask the user to enter a number and store it in `n`.
n= input ("enter a number")
n=int(n)
# 2) Set `sum` to 0.
sum=0
# (This will store the running total.)

# 3) Use a `for` loop from 1 to `n` (inclusive):
for q in range (1, n+1, 1):
# - In each step, add the current value of `i` to `sum`.
    sum=sum+q
# 4) After adding, print the current value of `sum`.
print (sum)
# (So the user can see how the sum increases step by step.)
for 