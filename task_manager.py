from prettytable import PrettyTable
from datetime import datetime

todays_date = datetime.now().strftime("%d %b %Y")
users_generated = 0
username = ""
username_list = []


def user_log_in():
    """Function to allow user log in"""
    global username  # Global function declared as utilised in other functions
    global username_list  # Declared as global as used in other functions
    user_read = open("user.txt", "r", encoding="utf-8")

    # Importing usernames and passwords from user.txt and saving them in two separate lists
    username_list = []
    password_list = []
    for line in user_read:
        user, psw = line.strip("\n").split(", ")
        username_list.append(user)
        password_list.append(psw)
    user_read.close()

    username = input("Please enter your username: ")
    # Using a while loop to validate their username
    while username not in username_list:
        print("Invalid username")
        username = input("Please enter your username: ")

    position = username_list.index(username)  # Finding index position of username

    password = input("Please enter your password: ")
    # Using a while loop to validate their password against username index position
    while password != password_list[position]:
        print("Incorrect password")
        password = input("Please enter your password: ")


def reg_user():
    """Function to allow new user registration"""
    global users_generated  # Global function declared-utilised when user enters "gr" to calculate all the users registered with task_manager
    new_user = input(
        "Please enter a new username: "
    )  # Obtaining new username from user
    # Error handling
    if new_user in username_list:
        print("This user already exists, please enter another username: ")
    else:
        new_pass = input("Please enter a new password: ")
        confirm_pass = input("Please re-enter password: ")

        if new_pass == confirm_pass:
            users_generated += 1
            # New user added to user.txt
            with open("user.txt", "a", encoding="utf-8") as user_file:
                user_file.write(f"\n{new_user}, {new_pass}")
            print("New user registered successfully!")

        else:
            print("Password does not match, try again")


def add_task():
    """Function to allow user to add a new task"""
    # Obtaining details of the new task from user
    user_task = input(
        "Please enter the username of the person whom the task is assigned to: "
    )
    task_tile = input("Please enter the task title: ")
    task_description = input("Please describe the task: ")
    task_due_date = input("Please enter the task due date (DD, MMM, YYYY): ")
    completed = input("Please enter Yes if completed or No if not completed: ")
    # New tasks added to tasks.txt
    with open("tasks.txt", "a", encoding="utf-8") as task_file:
        task_file.write(
            f"\n{user_task}, {task_tile}, {task_description}, {todays_date}, {task_due_date}, {completed}"
        )
    print("Task added successfully!")


def view_all():
    """Function to allow user to view all tasks"""
    task_read = open("tasks.txt", "r", encoding="utf-8")
    data = task_read.readlines()
    for pos, line in enumerate(
        data, 1
    ):  # Using enumerate to number the lines in tasks.txt
        # Splitting each line by the comma so that data can be utilised and written as below
        split_data = line.split(", ")
        output = f"____________[{pos}]____________\n"
        output += "\n"
        output += f"Task: \t\t{split_data[1]}\n"
        output += f"Assigned to: \t{split_data[0]}\n"
        output += f"Date assigned: \t{split_data[3]}\n"
        output += f"Due date: \t{split_data[4]}\n"
        output += "Task complete: \tNo\n"
        output += f"Task description: {split_data[2]}\n"
        output += "___________________________\n"
        print(output)
    task_read.close()


def view_mine():
    """Function to allow user to see their tasks"""
    task_read = open("tasks.txt", "r", encoding="utf-8")
    data = task_read.readlines()
    # Creating a list that contains tasks belonging to user
    my_tasks = [line for line in data if username == line.split(", ")[0]]
    # If no task is found for user, print message below
    if not my_tasks:
        print(f"No tasks found assigned to {username}")
        return
    # Using enumerate to number data in my_tasks list starting from 1
    # Splitting each line by comma space to be able to use the data as per output below
    for pos, line in enumerate(my_tasks, 1):
        split_data = line.split(", ")

        output = f"____________[{pos}]____________\n"
        output += "\n"
        output += f"Task: \t\t{split_data[1]}\n"
        output += f"Assigned to: \t{split_data[0]}\n"
        output += f"Date assigned: \t{split_data[3]}\n"
        output += f"Due date: \t{split_data[4]}\n"
        output += f"Task complete: \t{split_data[-1]}"
        output += f"Task description: {split_data[2]}\n"
        output += "___________________________\n"
        print(output)
    while True:
        # Asking user to choose a task number or enter -1 to return to main menu
        task_choice = input(
            "Please select a task number or enter -1 to return to the main menu: "
        )
        if task_choice == "-1":
            break
        # Casting task_choice to integer. Deducting 1 as we started task position at 1, to be user friendly
        task_choice = int(task_choice) - 1
        # If user enters a task number below 0 or above the task number in my_tasks, error message is displayed
        if task_choice < 0 or task_choice > len(my_tasks) - 1:
            print("You have selected an invalid task number, try again.")
            continue
        # Displaying the task belonging to the user which they have selected
        selected_task = my_tasks[task_choice]
        split_data = selected_task.split(", ")
        output = f"____________[{task_choice + 1}]____________\n"
        output += "\n"
        output += f"Task: \t\t{split_data[1]}\n"
        output += f"Assigned to: \t{split_data[0]}\n"
        output += f"Date assigned: \t{split_data[3]}\n"
        output += f"Due date: \t{split_data[4]}\n"
        output += f"Task complete: \t{split_data[-1]}"
        output += f"Task description: {split_data[2]}\n"
        output += "___________________________\n"
        print(output)
        # Asking user if they wish to edit task or mark as completed
        while True:
            output = f"_____[SELECT AN OPTION]____\n"
            output += "1- Edit task \n"
            output += "2- Mark as completed \n"
            output += "___________________________\n"

            choice = int(input(output))
            # Error message is displayed if user enters a number other that 1 and 2
            if choice <= 0 or choice >= 3:
                print("You have selected an invalid option, try again.")
                continue
            # Error message is displayed if task to be edited has been completed already
            if choice == 1 and split_data[-1] == "Yes\n":
                print("You can't edit completed tasks")
                continue
            # If user enters option 1 and task is yet to becompleted, display option to edit due date or user to whom task is assigned
            if choice == 1 and split_data[-1] == "No\n":
                output = f"_____[SELECT AN OPTION]____\n"
                output += "1- Edit due date \n"
                output += (
                    "2- Edit username of the person to whom the task is assigned \n"
                )
                output += "___________________________\n"
                edit_task_choice = int(input(output))

                # If user slects 1, ask user for new due date and overwrite previous due date in data
                if edit_task_choice == 1:
                    new_due_date = input("Please enter new due date (DD, MMM, YYYY): ")
                    split_data[4] = new_due_date
                    new_data = ", ".join(split_data)
                    data[task_choice] = new_data
                    print("Due date changed")
                # If user selects 2, ask user for new username and overwrite previous username in data
                elif edit_task_choice == 2:
                    change_user = input("Please enter the new username: ")
                    split_data[0] = change_user
                    new_data = ", ".join(split_data)
                    data[task_choice] = new_data
                    print("Username changed")
            # If user choses 2 to mark task as complete, overwrite split_data to "Yes" in data
            elif choice == 2:
                split_data[-1] = "Yes\n"
                new_data = ", ".join(split_data)
                data[task_choice] = new_data
                print("Task marked as completed")
            # Replace the data in tasks.txt with the new data
            task_write = open("tasks.txt", "w", encoding="utf-8")
            for line in data:
                task_write.write(line)

            task_write.close()
    task_read.close()


def display_statistics():
    """Function to allow user to see statistics in user_overview.txt"""
    combined = []
    task_over = open("task_overview.txt", "r", encoding="utf-8")
    user_over = open("user_overview.txt", "r", encoding="utf-8")
    # Strip and split each line from task_overwiew.txt and append to the list "combined"
    for line in task_over:
        data = line.strip("\n, _, ").split(", ")
        combined.append(data)

    # Strip and split each line from user_overwiew.txt and append to the list "combined"
    for line in user_over:
        data = line.strip("\n, _, ").split(", ")
        combined.append(data)
    # Using PrettyTable to display the combined data
    table = PrettyTable()
    for item in combined:
        table.add_row(item)

    print(table)

    task_over.close()
    user_over.close()


user_log_in()

# Using a while loop asking user to select from menu. User 'admin' to have additional options 'gr' and 'ds'
# Using if/elif/else statements for the option selected below
# If 'r' add new user to user.txt
# if 'a' add new task to tasks.txt
# if 'va' display all tasks
# if 'vm' display user own tasks
# if 'gr' and user 'admin' generate reports
# if 'ds' and user 'admin' display statistics
# if 'e' exit
while True:
    menu = "\nPlease select one of the following options:\n"
    menu += "r - register user\n"
    menu += "a - add task\n"
    menu += "va - view all tasks\n"
    menu += "vm - view my tasks\n"
    # Adding additional options for admin
    if username == "admin":
        menu += "gr - generate reports\n"
        menu += "ds - display statistics\n"
    menu += "e - exit\n"
    menu += ": "
    # Formatting text to lower to avoid errors
    menu_choice = input(menu).lower()
    # Function is called if user is admin and enters 'r'
    if menu_choice == "r" and username == "admin":
        reg_user()

    elif menu_choice == "r" and username != "admin":
        print("User not authorised to register other users")

    elif menu_choice == "a":
        add_task()

    elif menu_choice == "va":
        view_all()

    elif menu_choice == "vm":
        view_mine()

    elif menu_choice == "gr":
        task_over = open("task_overview.txt", "w", encoding="utf-8")
        task_read = open("tasks.txt", "r", encoding="utf-8")
        data = task_read.readlines()
        num_of_tasks = 0
        num_tasks_completed = 0
        num_tasks_not_completed = 0
        num_tasks_overdue = 0
        # Using a for loop to count the lines/tasks in tasks.txt
        for line in data:
            num_of_tasks += 1

        for line in data:
            # Splitting data to be able to use values separately
            split_data = line.split(", ")
            # Variable stores the due date in %d %b %Y format
            due_date = datetime.strptime(split_data[4], "%d %b %Y").date()
            # Casting todays_date from string to object
            todays_date_obj = datetime.strptime(todays_date, "%d %b %Y").date()
            # If task is completed, it adds 1 to num_tasks_completed
            if split_data[-1] == "Yes\n":
                num_tasks_completed += 1
            # If task is not completed, it adds 1 to num_tasks_not_completed
            elif split_data[-1] == "No\n":
                num_tasks_not_completed += 1
            # If task is not completed and it is overdue, it adds 1 to num_tasks_overdue
            if split_data[-1] == "No\n" and due_date < todays_date_obj:
                num_tasks_overdue += 1
        # Calculating percentage of tasks not completed and percentage overdue and creating output in task_overiew.txt
        percentage_not_completed = num_tasks_not_completed / len(data) * 100
        percentage_overdue = num_tasks_overdue / len(data) * 100
        output = "_______________________\n"
        output += f"Total number of tasks: {num_of_tasks}\n"
        output += "_______________________\n"
        output += f"Number of tasks completed: {num_tasks_completed}\n"
        output += "_______________________\n"
        output += f"Number of tasks not yet completed: {num_tasks_not_completed}\n"
        output += "_______________________\n"
        output += f"Number of tasks overdue: {num_tasks_overdue}\n"
        output += "_______________________\n"
        output += (
            f"Percentage of tasks not completed: {int(percentage_not_completed)}%\n"
        )
        output += "_______________________\n"
        output += f"Percentage of overdue tasks: {int(percentage_overdue)}%\n"
        output += "_______________________\n"
        task_over.write(output)
        task_over.close()
        task_read.close()
        # Write the number of new users generated with task_manager.py into user_overview.txt
        # Write the number of tasks into user_overview.txt
        user_over = open("user_overview.txt", "w", encoding="utf-8")
        output = "_______________________\n"
        output += f"Total number of users registered: {users_generated}\n"
        output += "_______________________\n"
        output += f"Total number of tasks generated: {num_of_tasks}\n"
        user_over.write(output)

        # Creating dictionaries that contain the total number of tasks, the number of tasks completed, non completed and overdue
        task_count = {}
        completed_count = {}
        incomplete_count = {}
        user_overdue_count = {}
        output = ""
        # For each task in data, variables are created for each element
        for line in data:
            user, task, description, assigned, due, completed = line.strip().split(", ")
            # Addind 1 to task_count for each user task
            if user in task_count:
                task_count[user] += 1
            else:
                task_count[user] = 1
                # If task is completed, 1 is added to that user in completed_count
                if completed == "Yes":
                    if user in completed_count:
                        completed_count[user] += 1
                    else:
                        completed_count[user] = 1
                # If task is not completed, 1 is added to that user in incomplete_count
                if completed == "No":
                    if user in incomplete_count:
                        incomplete_count[user] += 1
                    else:
                        incomplete_count[user] = 1
            # If task is not completed and it's overdue, 1 is added to that user in user_overdue_count
            if completed == "No" and due < todays_date:
                if user in user_overdue_count:
                    user_overdue_count[user] += 1

        # Output the above into user_overwiew.txt as below
        for user in task_count:
            output += "_______________________\n"
            output += f"Total number of tasks assigned to {user}: {task_count[user]}\n"

            # Calculating the percentage of tasks assigned to each user dividing by the total tasks
            user_tasks_percentage = task_count[user] / num_of_tasks * 100
            output += "_______________________\n"
            output += f"Percentage of tasks assigned to {user}: {int(user_tasks_percentage)}%\n"

            user_completed_tasks = completed_count.get(user, 0)
            # Calculating the percentage of completed tasks for each user dividing by the num of tasks assigned to that user
            completed_tasks_percentage = user_completed_tasks / task_count[user] * 100
            output += "_______________________\n"
            output += f"Percentage of completed tasks assigned to {user}: {int(completed_tasks_percentage)}%\n"

            user_incomplete_tasks = incomplete_count.get(user, 0)
            # Calculating the percentage of not completed tasks for each user dividing by the num of tasks assigned to that user
            incomplete_tasks_percentage = user_incomplete_tasks / task_count[user] * 100
            output += "_______________________\n"
            output += f"Percentage of incomplete tasks assigned to {user}: {int(incomplete_tasks_percentage)}%\n"

            user_overdue_tasks = user_overdue_count.get(user, 0)
            # Calculating percentage of user overdue tasks dividing by user total tasks
            user_overdue_percentage = user_overdue_tasks / task_count[user] * 100
            output += "_______________________\n"
            output += f"Percentage of overdue tasks assigned to {user}: {int(user_overdue_percentage)}%\n"

        user_over.write(output)
        user_over.close()
        task_read.close()

    elif menu_choice == "ds" and username == "admin":
        display_statistics()

    elif menu_choice == "e":
        print("Goodbye")
        exit()

    else:
        print("Incorrect selection, please try again!")
