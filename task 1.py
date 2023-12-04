def show_menu():
    print("1. View to-do list")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Exit")

def view_todo_list():
    with open("todo.txt", "r") as file:
        tasks = file.readlines()
        if tasks:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
        else:
            print("Your to-do list is empty.")

def add_task():
    task = input("Enter the task: ")
    with open("todo.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully.")

def mark_task_done():
    view_todo_list()
    task_number = int(input("Enter the task number to mark as done: ")) - 1

    with open("todo.txt", "r") as file:
        tasks = file.readlines()

    if 0 <= task_number < len(tasks):
        completed_task = tasks.pop(task_number)
        with open("todo.txt", "w") as file:
            file.writelines(tasks)

        with open("done.txt", "a") as file:
            file.write(completed_task)
        print("Task marked as done.")
    else:
        print("Invalid task number.")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        view_todo_list()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_task_done()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
def show_menu():
    print("1. View to-do list")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Exit")

def view_todo_list():
    with open("todo.txt", "r") as file:
        tasks = file.readlines()
        if tasks:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
        else:
            print("Your to-do list is empty.")

def add_task():
    task = input("Enter the task: ")
    with open("todo.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully.")

def mark_task_done():
    view_todo_list()
    task_number = int(input("Enter the task number to mark as done: ")) - 1

    with open("todo.txt", "r") as file:
        tasks = file.readlines()

    if 0 <= task_number < len(tasks):
        completed_task = tasks.pop(task_number)
        with open("todo.txt", "w") as file:
            file.writelines(tasks)

        with open("done.txt", "a") as file:
            file.write(completed_task)
        print("Task marked as done.")
    else:
        print("Invalid task number.")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        view_todo_list()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_task_done()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
def show_menu():
    print("1. View to-do list")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Exit")

def view_todo_list():
    with open("todo.txt", "r") as file:
        tasks = file.readlines()
        if tasks:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
        else:
            print("Your to-do list is empty.")

def add_task():
    task = input("Enter the task: ")
    with open("todo.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully.")

def mark_task_done():
    view_todo_list()
    task_number = int(input("Enter the task number to mark as done: ")) - 1

    with open("todo.txt", "r") as file:
        tasks = file.readlines()

    if 0 <= task_number < len(tasks):
        completed_task = tasks.pop(task_number)
        with open("todo.txt", "w") as file:
            file.writelines(tasks)

        with open("done.txt", "a") as file:
            file.write(completed_task)
        print("Task marked as done.")
    else:
        print("Invalid task number.")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        view_todo_list()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_task_done()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
def show_menu():
    print("1. View to-do list")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Exit")

def view_todo_list():
    with open("todo.txt", "r") as file:
        tasks = file.readlines()
        if tasks:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
        else:
            print("Your to-do list is empty.")

def add_task():
    task = input("Enter the task: ")
    with open("todo.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully.")

def mark_task_done():
    view_todo_list()
    task_number = int(input("Enter the task number to mark as done: ")) - 1

    with open("todo.txt", "r") as file:
        tasks = file.readlines()

    if 0 <= task_number < len(tasks):
        completed_task = tasks.pop(task_number)
        with open("todo.txt", "w") as file:
            file.writelines(tasks)

        with open("done.txt", "a") as file:
            file.write(completed_task)
        print("Task marked as done.")
    else:
        print("Invalid task number.")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        view_todo_list()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_task_done()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
v