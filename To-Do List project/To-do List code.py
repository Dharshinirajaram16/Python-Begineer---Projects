#------------------------To-Do List in Python------------------


tasks = []
def show_task():
    print("\n----To-Do List in Python----")
    print("1. Add a task")
    print("2. View a task")
    print("3. Mark a task")
    print("4. Remove a task")
    print("5. Exit")

def add_task():
    task = input("Enter a task: ")
    tasks.append({"task":task, "done":False})
    print(f"Task added: {task}")

def view_task():
    if not tasks:
        print("No tasks yet!")
        return
    print("\n Your Tasks ")
    for index,task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        print(f"{index}. {task['task']} | {status}") #....

def mark_done():
    view_task()
    if not tasks:
        return
    try:
        index = int (input("Enter a task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("Marked as done!")
        else:
           print("Invalid task!")
    except ValueError:
        print("Please enter a valid task number!")

def delete_task():
    view_task()
    if not tasks:
        return
    try:
        index = int (input("Enter a task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            remove = tasks.pop(index)
            print(f"Delete task: {remove['task']}")
        else:
            print("Invalid task!")
    except ValueError:
        print("Please enter a valid task number!")

while True:
    show_task()
    choice = input("Choose an option (1-5): ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("thank you for using this program")
        break
    else:
        print("Invalid option!, try again")
