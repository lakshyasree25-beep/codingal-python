print("Library Visit Planner")

day = input("What day is it? ")

if day == "friday" or day == "saturday" or day == "sunday":
    print("The weekend is a good time to visit the library!")
elif day == "monday" or day == "tuesday" or day == "wednesday":
    print("Good day to study at the library!")

weather = input("How is the weather? ")
book = input("Do you need to return a book? ")

if weather == "sunny" and book == "yes":
    print("It's a good time to give the book back!")
elif weather == "rainy" or weather == "cloudy":
    print("Remember to bring an umbrella!")

if book == "no":
    print("good job you don't need to return a book!")