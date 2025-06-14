def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {task['title']} {status}")

def add_task(tasks):
    title = input("Enter task name: ")
    tasks.append({"title": title, "done": False})
    print(f"Task '{title}' added.")

def mark_task_done(tasks):
    view_tasks(tasks)
    try:
        choice = int(input("Enter task number to mark as done: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["done"] = True
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    main()
