tasks = []

while True:

    print("""
1. Add Task
2. Display Tasks
3. Edit Task
4. Delete Task
5. Exit
""")

    choice = int(input("Enter a number between 1-5: "))

    if choice == 1:

        while True:
            task = input("Enter your task (q to quit): ")

            if task.lower() == "q":
                break

            tasks.append(task)
            print("Task added successfully!")

    elif choice == 2:

        if tasks:
            print(tasks)
        else:
            print("There are no tasks to display.")

    elif choice == 3:

        task_name = input("Enter the task to edit: ")

        if task_name in tasks:
            index = tasks.index(task_name)

            new_task = input("Enter the new task: ")
            tasks[index] = new_task

            print("Task updated successfully!")
        else:
            print("Task not found!")

    elif choice == 4:

        task_name = input("Enter the task to delete: ")

        if task_name in tasks:
            tasks.remove(task_name)
            print("Task deleted successfully!")
        else:
            print("Task not found!")

    elif choice == 5:
        break

    else:
        print("Invalid number.")

print("----- Thank You -----")