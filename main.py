
tasks = []
next_id = 1


def add_task(title):
    global next_id

    task = {
        "id": next_id,
        "title": title,
        "completed": False
    }

    tasks.append(task)
    next_id += 1
    return task


def display_tasks():
    if not tasks:
        print("No tasks available.")
        return

    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        print(f'{task["id"]}. {task["title"]} - {status}')


def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                return False

            task["completed"] = True
            return True

    return False


def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return True

    return False


def main():
    while True:
        print("\n===== Student Task Manager =====")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            task = add_task(title)
            print(f'Task added with ID {task["id"]}.')

        elif choice == "2":
            display_tasks()

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID: "))
                if complete_task(task_id):
                    print("Task completed successfully.")
                else:
                    print("Task not found.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            try:
                task_id = int(input("Enter task ID: "))
                if delete_task(task_id):
                    print("Task deleted successfully.")
                else:
                    print("Task not found.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
