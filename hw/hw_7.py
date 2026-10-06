secret = 27
max_attempts = 5
count = 0
guess = 0

print("Guess the number")

while count < max_attempts and guess != secret:
guess = int(input("Guess: "))
count = count + 1

if guess == secret:
    print("You got it!")
else:
    if guess > secret:
        diff = guess - secret
    else:
        diff = secret - guess

    if diff >= 20:
        print("Ice cold")
    elif diff >= 10:
        print("Cold")
    elif diff >= 5:
        print("Warm")
    else:
        print("Hot")

    left = max_attempts - count

if guess != secret:
print("Game over")
print("number", secret)
