#Step 1: Define and call greet_customer() to welcome every customer to the stand.
def greet_customer():
  print("Welcome to my lemanad stand")
greet_customer()
#Step 2: Ask for the price per cup and the number of cups sold.
input ("what price of cup do you want: ")
input ("how many cups do you want?")
#Step 3: Define and call calculate_total() to return the total cost using arguments.\
def calculate_total(price, number_of_cups):
  return price * number_of_cups
#Step 4: Round the total using the built-in round() function and print it.

#Step 5: Define and call calculate_change() to return the change due.
def calculate_change(total, amount_paid):
  return amount_paid - total
#Step 6: Define and call thank_you_message() to return a personalized closing line.
def thank_you(name):
  print("Thank you",name)  
#Step 7: Print the final lemonade stand receipt with every calculated value.
print("===== LEMONADE STAND RECEIPT =====")
print("Total:", total)
print("Change:", calculate_change(total, input("Amount paid:")))
print("Thank you", name)