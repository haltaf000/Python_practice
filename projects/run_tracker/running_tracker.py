# I want to create a running tracker application since I want to improve my one mile run time but want to add more features!
# The application can record time and distance  
# Along with the ability to delete, edit, add, etc.... 
# This application just doesnt have to calculate one mile but multiple forms of run. 
import json

running_time = {}
weight_in_lbs = {}
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
    if weight_in_lbs:
        for key in weight_in_lbs:
            print(f"Day {key}: weight {weight_in_lbs[key]} ")


# Delete selected Items

def delete_something():
    delete_what = input("What would you like the delete? 'run' or 'weight': ").lower()
    if delete_what == 'run':
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
    elif delete_what == 'weight':
        if weight_in_lbs:
            what_day = int(input("What day do you want to delete? "))
            if what_day in weight_in_lbs:
                del weight_in_lbs[what_day]
                print(f"Day {what_day} is removed from the log!")
            else:
                print(f"{what_day} does not exist!")
                save_data()
        else:
            print("No weight history!")


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

# Add function to keep log of your weight

def weight_check():
    weight = float(input("What is your weight in lbs: "))
    what_day_check = int(input("What day did you check? "))
    weight_in_lbs[what_day_check] = weight

# Save data the user has input

def save_data():
    data = {
        "running_time": running_time,
        "weight_in_lbs": weight_in_lbs
    }
    with open("running_data.json", "w") as f:
        json.dump(data, f)
    print("Data saved successfully.")

def load_data():
    global running_time, weight_in_lbs, run_counter
    try:
        with open("running_data.json", "r") as f:
            data = json.load(f)
        running_time = {int(k): v for k, v in data.get("running_time", {}).items()}
        weight_in_lbs = {int(k): v for k, v in data.get("weight_in_lbs", {}).items()}
        run_counter = max(running_time.keys()) + 1 if running_time else 1
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("No saved data found. Starting with empty logs.")
        running_time = {}
        weight_in_lbs = {}
        run_counter = 1
    except json.JSONDecodeError:
        print("Error decoding JSON file. Starting with empty data.")
        running_time = {}
        weight_in_lbs = {}
        run_counter = 1


run = True

while run:
    question = input("What would you like to do today? Type 'add', 'check', 'save', 'load', 'edit', 'report', 'delete', 'weight', 'off': ").lower()

    if question == 'add':
        add_time()
    elif question =='check':
        check_latest_time()
    elif question == 'delete':
         delete_something()
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
    elif question == "weight":
        weight_check()
    else:
        print("Incorrect input! Choose from the options.")