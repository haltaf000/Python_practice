print("Welcome to the tip Calculator!")
bill = float(input("What was the total bill? "))

tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
how_many_split = int(input('How many people to split the bill? '))

total = bill + (bill * tip / 100)

total_bill = round(total/how_many_split, 2)


print(f"Each person should pay: ${total_bill}")


