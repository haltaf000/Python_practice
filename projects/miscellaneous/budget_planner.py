budget_type = {}

income_type = {}

def income():
    job = input("What type of job do you have? ")
    income = float(input("How much money do you make per month? ")) 
    income_type[job] = income

def expenses():
    pass


def transactions():
    pass

def budget():
    while True: 
        question = input("What will you like to do? type 'add' or 'done': ")
        if question == 'add':
            category = input("Enter a budget category: ")
            amount = int(input("Enter the amount to be spent monthly: "))
            budget_type[category] = amount
        elif question == 'done':
            break
        else:
            print("Incorrect input: Type 'add'  or 'done'")

def report():
    if income_type:
        total_income = 0
        for key in income_type:
            value = income_type[key]
            total_income += value
            print(f"Current jobs: {key}")
            print(f"With total income of {total_income}")
    else:
        print('No income sources recorded! \n')

    if budget_type:
        total_budget = 0
        for key in budget_type:
            values = budget_type[key]
            total_budget += values
            print(f"For {key} = allocated: {values}")
        print(f"The total budget is: {total_budget} ")
    else:
        print("\n")
        print("There is no budget planned!\n")

budget_on = True

while budget_on:
    choice = input("\nWhat would you like to do today? Type 'income', 'expenses', 'transactions', 'budget', 'report', 'off': ")

    if choice == 'off':
        budget_on = False
    elif choice == "income":
        income()
    elif choice == 'expenses':
        expenses()
    elif choice == "transactions":
        transactions()
    elif choice == 'budget':
        budget()
    elif choice == 'report':
        report()
    else:
        print("Invalid choice. Please choose from 'income', 'expenses', 'transactions', 'budget', 'report', or 'off'.")