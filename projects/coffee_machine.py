MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Coffee Machine Resources

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Create Monetary Values
coins = {
    'penny': 0.01,
    'nickel': 0.05,
    'dime': 0.10,
    'quarter': 0.25,
}

# Total Money
money = 0

# Create a Report
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


# Do the Calculations

def calculations(choice, item):
    money = money
    total_input = 0
    item_cost = item['cost']

    while total_input < item_cost:
        print("Please insert coins: ")
        how_many_quarters = int(input("How many quarters: "))
        how_many_dimes = int(input("How many dimes: "))
        how_many_nickels = int(input("How many nickels: "))
        how_many_pennies = int(input("How many pennies: "))

        total_input += (how_many_dimes * coins['dime']) + (how_many_pennies * coins['penny']) +  (how_many_quarters * coins['quarter']) + (how_many_nickels * coins['nickel'])

        if total_input < item_cost:
            how_much_required = item_cost - total_input
            refund = total_input - how_much_required
            print(f"You still owe ${how_much_required}. Here is your refund ${refund}")
            break
        elif total_input > item_cost:
            too_much = round(total_input - item_cost, 2)
            total_input -= too_much
            print(f"Here is your change ${too_much}")
            money += item_cost
            print(f"Here is your {choice}! Enjoy!")
        else:
            money += item_cost
            print(f"Here is your {choice}! Enjoy!")

        if 'water' in item['ingredients']:
            resources['water'] -= item['ingredients']['water']
        if 'coffee' in item['ingredients']:
            resources['coffee'] -= item['ingredients']['coffee']
        if 'milk' in item['ingredients']:
            resources['milk'] -= item['ingredients']['milk']


# Check the resources if they are enough to make the product!

def item_check(choice, item):
    if 'water' in item['ingredients'] and resources['water'] < item['ingredients']['water']:
        print("Sorry there is not enough water!")
    elif 'coffee' in item['ingredients'] and resources['coffee'] < item['ingredients']['coffee']:
        print("Sorry there is not enough water!")
    elif 'milk' in item['ingredients'] and resources['milk'] < item['ingredients']['milk']:
            print("Sorry there is not enough coffee!")
    else:
        calculations(choice, item)


# State of Coffee machine
machine_is_on = True

# Create a while loop while machine is on

while machine_is_on:
    choice = input("What would you like? (espresso / latte / cappuccino):  ").lower()

    if choice == "report":
        report()

    elif choice == "off":
        machine_is_on = False

    # input the calculations function
    else:
        item_check(choice, MENU[choice])



'''
    if choice == "espresso":
        if resources['water'] < MENU['espresso']['ingredients']['water']:
            print("Sorry there is not enough water!")
        elif resources['coffee'] < MENU['espresso']['ingredients']['coffee']:
            print("Sorry there is not enough coffee!")
        else:
            total_input = 0
            item_cost = MENU['espresso']['cost']

            while total_input < item_cost:
                print("Please insert coins: ")
                how_many_quarters = int(input("How many quarters: "))
                how_many_dimes = int(input("How many dimes: "))
                how_many_nickels = int(input("How many nickels: "))
                how_many_pennies = int(input("How many pennies: "))

                total_input += (how_many_dimes * dime) + (how_many_pennies * penny) +  (how_many_quarters * quarter) + (how_many_nickels * nickel)

                if total_input < item_cost:
                    how_much_required = item_cost - total_input
                    refund = total_input - how_much_required
                    print(f"You still owe ${how_much_required}. Here is your refund ${refund}")
                    break
                elif total_input > item_cost:
                    too_much = round(total_input - item_cost, 2)
                    print(f"Here is your change ${too_much}")
                    money += item_cost
                    print("Here is your espresso! Enjoy!")
                else:
                    money += item_cost
                    print("Here is your espresso! Enjoy!")

                resources['water'] -= MENU['espresso']['ingredients']['water']
                resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
                



    if choice == "latte":
        if resources['water'] < MENU['latte']['ingredients']['water']:
            print("Sorry there is not enough water!")
        elif resources['milk'] < MENU['latte']['ingredients']['milk']:
            print("Sorry there is not enough coffee!")
        elif resources['coffee'] < MENU['latte']['ingredients']['coffee']:
            print("Sorry there is not enough coffee!")
        else:
            total_input = 0
            item_cost = MENU['latte']['cost']

            while total_input < item_cost:
                print("Please insert coins: ")
                how_many_quarters = int(input("How many quarters: "))
                how_many_dimes = int(input("How many dimes: "))
                how_many_nickels = int(input("How many nickels: "))
                how_many_pennies = int(input("How many pennies: "))

                total_input += (how_many_dimes * dime) + (how_many_pennies * penny) +  (how_many_quarters * quarter) + (how_many_nickels * nickel)

                if total_input < item_cost:
                    how_much_required = item_cost - total_input
                    refund = total_input - how_much_required
                    print(f"You still owe ${how_much_required}. Here is your refund {refund}")
                    break
                elif total_input > item_cost:
                    too_much = round(total_input - item_cost, 2)
                    print(f"Here is your change ${too_much}")
                    money += item_cost
                    print("Here is your latte! Enjoy!")
                else:
                    money += item_cost
                    print("Here is your latte! Enjoy!")

                resources['water'] -= MENU['latte']['ingredients']['water']
                resources['coffee'] -= MENU['latte']['ingredients']['coffee']
                resources['milk'] -= MENU['latte']['ingredients']['milk']



    if choice == "cappuccino":
        if resources['water'] < MENU['cappuccino']['ingredients']['water']:
            print("Sorry there is not enough water!")
        elif resources['milk'] < MENU['cappuccino']['ingredients']['milk']:
            print("Sorry there is not enough coffee!")
        elif resources['coffee'] < MENU['cappuccino']['ingredients']['coffee']:
            print("Sorry there is not enough coffee!")
        else:
            total_input = 0
            item_cost = MENU['cappuccino']['cost']

            while total_input < item_cost:
                print("Please insert coins: ")
                how_many_quarters = int(input("How many quarters: "))
                how_many_dimes = int(input("How many dimes: "))
                how_many_nickels = int(input("How many nickels: "))
                how_many_pennies = int(input("How many pennies: "))

                total_input += (how_many_dimes * dime) + (how_many_pennies * penny) + (how_many_quarters * quarter) + (
                            how_many_nickels * nickel)

                if total_input < item_cost:
                    how_much_required = item_cost - total_input
                    refund = total_input - how_much_required
                    print(f"You still owe ${how_much_required}. Here is your refund {refund}")
                    break
                elif total_input > item_cost:
                    too_much = round(total_input - item_cost, 2)
                    print(f"Here is your change ${too_much}")
                    money += item_cost
                    print("Here is your cappuccino! Enjoy!")
                else:
                    money += item_cost
                    print("Here is your cappuccino! Enjoy!")

                resources['water'] -= MENU['cappuccino']['ingredients']['water']
                resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
                resources['milk'] -= MENU['cappuccino']['ingredients']['milk']


'''
    

