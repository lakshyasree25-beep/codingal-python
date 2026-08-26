#Step 1: Print the welcome message: "=== Smart School Day Planner ==="""
print ("welcome to Smart School Day Planner ")
#Step 2: Use input() to ask for the day, weather, and homework status. Store each in a variable.
day=input ("what day is it")
weather=input ("how is the weather")
Homework_status= input ("have you done your homework\n")
#Step 4: Write if-elif-else to classify the day type (weekend / Monday / Friday / other school day).
if day== "saturday" or day=="sunday":
    print ("take a break")
elif day=="monday":
    print ("do your homeyork first")
elif day=="friday":
    print("have a good weekend")
else:
    print ("hang in there")
#Step 5: Write an if statement using AND to check sunny weather and homework done together.
if Homework_status=="yes" and weather== "sunny":
    print("you can go out to play")
elif Homework_status=="no" and weather== "sunny":
    print ("do your homework and then you can play outside")
elif Homework_status=="yes" and weather== "rainy":
    print ("play inside")
elif Homework_status=="no" and weather== "rainy":
    print ("do your homewor and then play inside")
#Step 6: Write an if statement using OR to check rainy or cloudy weather.
if weather=="rainy" or weather=="cloudy":
    print ("bring an umbrella")
#Step 7: Write an if statement using NOT to catch when homework is not done.
if not (Homework_status== "yes"):
    print ("do your homework")
#Step 8: Write if-elif-else using AND, OR, and NOT combined to print the best plan message.
#Step 9: Print the closing message: "Plan complete! Have a wonderful day!"
print ("Plan completed! Have a wonderful day!")
#Step 10: Run the program with three different combinations of inputs to test all branches."""