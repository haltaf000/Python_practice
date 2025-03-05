import json

class RunTracker:
    def __init__(self):
        self.running_time = {}
        self.run_counter = 1

    def add_time(self):
        try:
            hour = int(input("Input how many hours ran: "))
            minutes = int(input("Input how many minutes: "))
            seconds = int(input("Input how many seconds: "))
        except ValueError:
            print("Please enter valid numbers for time.")
            return

        # Format time with leading zeros
        time_str = f"{hour:02}:{minutes:02}:{seconds:02}"

        try:
            distance = float(input("Add distance in miles: "))
        except ValueError:
            print("Please enter a valid distance.")
            return

        self.running_time[self.run_counter] = {'time': time_str, "distance": distance}
        self.run_counter += 1

    def check_latest_time(self):
        if self.running_time:
            latest_run = max(self.running_time.keys())
            run_data = self.running_time[latest_run]
            print(f"Day: {latest_run} = Ran {run_data['distance']} miles in {run_data['time']}")
        else:
            print("Please start recording your runs!")

    def report(self):
        if self.running_time:
            for key in self.running_time:
                run_data = self.running_time[key]
                print(f"Day: {key} = Ran {run_data['distance']} miles in {run_data['time']}")
        else:
            print("No running history!")

    def delete_time(self):
        if self.running_time:
            try:
                delete_day = int(input("What day do you want to delete? "))
            except ValueError:
                print("Please enter a valid day number.")
                return
            if delete_day in self.running_time:
                del self.running_time[delete_day]
                print(f"Day {delete_day} is removed from the log!")
            else:
                print(f"Day {delete_day} does not exist!")
        else:
            print("No running history!")

    def edit_time(self):
        if self.running_time:
            try:
                run_day = int(input("What day do you want to edit? "))
            except ValueError:
                print("Please enter a valid day number.")
                return

            if run_day in self.running_time:
                try:
                    hour = int(input("Input how many hours ran: "))
                    minutes = int(input("Input how many minutes: "))
                    seconds = int(input("Input how many seconds: "))
                except ValueError:
                    print("Please enter valid numbers for time.")
                    return

                # Format time consistently
                time_str = f"{hour:02}:{minutes:02}:{seconds:02}"
                
                try:
                    distance = float(input("Add distance in miles: "))
                except ValueError:
                    print("Please enter a valid distance.")
                    return

                self.running_time[run_day] = {'time': time_str, "distance": distance}
                print(f"Updated run on day {run_day}: Ran {distance} miles in {time_str}")
            else:
                print(f"Day {run_day} does not exist!")
        else:
            print("No running history!")

    # Save data the user has input

    def save_data(self):
        with open("running_data.json", "w") as f:
            json.dump(self.running_time, f)


    # Load the data user has stored.

    def load_data(self):
        try:
            with open("running_data.json", "r") as f:
                data = json.load(f)
            self.running_time = {int(k): v for k, v in data.items()}
            self.run_counter = max(self.running_time.keys()) + 1 if self.running_time else 1
        except FileNotFoundError:
            self.running_time = {}
            self.run_counter = 1


# Main program loop
tracker = RunTracker()
run = True

while run:
    question = input("What would you like to do today? Type 'add', 'check', 'edit', 'report', 'delete', 'off': ").lower()

    if question == 'add':
        tracker.add_time()
    elif question == 'check':
        tracker.check_latest_time()
    elif question == 'delete':
        tracker.delete_time()
        tracker.save_data() 
    elif question == 'report':
        tracker.report()
    elif question == 'edit':
        tracker.edit_time()
    elif question == 'save':
        tracker.save_data()
    elif question == 'load':
        tracker.load_data()
    elif question == 'off':
        run = False
    else:
        print("Incorrect input! Choose from the options.")
