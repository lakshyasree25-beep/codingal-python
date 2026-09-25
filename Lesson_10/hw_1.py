print("Grocery Billing")

low = 0
medium = 0
high = 0
customers = 0
sales = 0

name = input("Name: ")
items = int(input("Items: "))

if items > 0:
    total = 0
    n = 1

    while n <= items:
        item = input("Item: ")
        price = int(input("Price: "))
        quantity = int(input("Quantity: "))

        if price > 0 and quantity > 0:
            cost = price * quantity
            print(item, cost)
            total += cost

            if cost < 50:
                low += 1
            elif cost <= 100:
                medium += 1
            else:
                high += 1

        n += 1

    customers += 1
    sales += total
    print("Total:", total)

print("Report")
print("Customers:", customers)
print("Sales:", sales)