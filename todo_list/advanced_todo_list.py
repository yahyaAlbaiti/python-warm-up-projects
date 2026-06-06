tasks = []

def add():
    while True:
        task = input("Enter your task (q to quit): ")

        if task.lower() == "q":
            break

        tasks.append({
            "name": task,
            "status": False
        })

        print("Task added successfully!")


def display():
    if not tasks:
        print("There are no tasks to display.")
        return

    print("\n----- Tasks -----")

    for i, task in enumerate(tasks, start=1):
        symbol = "[✔]" if task["status"] else "[✘]"
        print(f"{i}. {symbol} {task['name']}")


def edit():
    if not tasks:
        print("There are no tasks to edit.")
        return

    display()

    task_num = int(input("Enter task number to edit: "))

    if 1 <= task_num <= len(tasks):
        tasks[task_num - 1]["name"] = input("Enter the new task: ")
        print("Task updated successfully!")
    else:
        print(f"Invalid number. Choose between 1 and {len(tasks)}.")


def delete():
    if not tasks:
        print("There are no tasks to delete.")
        return

    display()

    task_num = int(input("Enter task number to delete: "))

    if 1 <= task_num <= len(tasks):
        tasks.pop(task_num - 1)
        print("Task deleted successfully!")
    else:
        print(f"Invalid number. Choose between 1 and {len(tasks)}.")


def complete():
    if not tasks:
        print("There are no tasks to complete.")
        return

    display()

    task_num = int(input("Enter task number to complete: "))

    if 1 <= task_num <= len(tasks):
        tasks[task_num - 1]["status"] = True
        print("Task completed!")
    else:
        print(f"Invalid number. Choose between 1 and {len(tasks)}.")


while True:
    print("""
1. Add Task
2. Display Tasks
3. Edit Task
4. Delete Task
5. Complete Task
6. Exit
""")

    user_choice = int(input("Enter a number from the menu: "))

    if user_choice == 1:
        add()
    elif user_choice == 2:
        display()
    elif user_choice == 3:
        edit()
    elif user_choice == 4:
        delete()
    elif user_choice == 5:
        complete()
    elif user_choice == 6:
        break
    else:
        print("Invalid choice. Enter a number from 1 to 6.")

print("----- Thank You -----")