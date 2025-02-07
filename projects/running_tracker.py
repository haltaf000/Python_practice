# I want to create a running tracker application since I want to improve my one mile run time but want to add more features!
# The application can record time and distance  
# Along with the ability to delete, edit, add, etc.... 
# This application just doesnt have to calculate one mile but multiple forms of run. 
import matplotlib.pyplot as plt
import json

running_time = {}
run_counter = 1

# To add time to your run log!
def add_time():
    global run_counter
    hour = int(input("Input how many hours ran: "))
    minutes = int(input("Input how many minutes: "))
    seconds = int(input("Input how many seconds: "))
    time = f"{hour:02}:{minutes:02}:{seconds:02}"

    distance = float(input("Add distance in miles: "))

    running_time[run_counter] = {'time': time, "distance":distance}
    run_counter += 1

# To check your latest run time!

def check_latest_time():
    if running_time:
        latest_run = max(running_time.keys())
        print(f"Day: {latest_run} = Ran {running_time[latest_run]['distance']} miles in {running_time[latest_run]['time']}")
    else:
        print("Please start recording your runs!")


# Develop a thorough report!

def report():
    if running_time:
        for key in running_time:
                print(f"Day: {key} = Ran {running_time[key]['distance']} miles in {running_time[key]['time']}")
    else:
        print("No running history!")


# Delete selected Items

def delete_time():
    if running_time:
        delete_day = int(input("What day do you want to delete? "))
        if delete_day in running_time:
            del running_time[delete_day]
            print(f"Day {delete_day} is removed from the log!")
        else:
            print(f"{delete_day} does not exist!")
            save_data() 
    else:
        print("No running history!")


# Edit Items that need to be changed

def edit_time():
    if running_time:
        run_day = int(input("What day do you want to edit? "))
        if run_day in running_time:
            hour = int(input("Input how many hours ran: "))
            minutes = int(input("Input how many minutes: "))
            seconds = int(input("Input how many seconds: "))
            time = str(hour) + ":" + str(minutes) + ':' + str(seconds)

            distance = int(input("Add distance in miles: "))

            running_time[run_day] = {'time': time, "distance":distance}
            
            print(f"Updated run on day {run_day} Ran {running_time[run_day]['distance']} miles in {running_time[run_day]['time']}")
        else:
            print(f"{run_day} does not exist!")
    else:
        print("No running history!")

# Save data the user has input

def save_data():
    with open("running_data.json", "w") as f:
        json.dump(running_time, f)


# Load the data user has stored.

def load_data():
    global running_time, run_counter
    try:
        with open("running_data.json", "r") as f:
            data = json.load(f)
        running_time = {int(k): v for k, v in data.items()}
        run_counter = max(running_time.keys()) + 1 if running_time else 1
    except FileNotFoundError:
        running_time = {}
        run_counter = 1


run = True

while run:
    question = input("What would you like to do today? Type 'add', 'check', 'save', 'load', 'edit', 'report', 'delete', 'off': ").lower()

    if question == 'add':
        add_time()
    elif question =='check':
        check_latest_time()
    elif question == 'delete':
         delete_time()
    elif question == 'report':
         report()
    elif question == 'edit':
        edit_time()
    elif question == 'save':
        save_data()
    elif question == 'load':
        load_data()
    elif question == 'off':
        run = False
    else:
        print("Incorrect input! Choose from the options.")