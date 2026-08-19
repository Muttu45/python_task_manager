from task_manager_app import Task, load_tasks, save_tasks
from task_manager_app.input_validator import (
    validate_confirmation,
    validate_numeric_input,
    validate_priority,
    validate_string_input
)


TASK_NAME_PATTERN = r"[A-Za-z0-9][A-Za-z0-9 .,'!?()-]*"


def display_menu():
    print("\n" + "=" * 35)
    print("      TASK MANAGER APPLICATION")
    print("=" * 35)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    print("=" * 35)


def add_task(tasks):
    print("\n--- Add New Task ---")

    name = validate_string_input(
        "Enter task name: ",
        pattern=TASK_NAME_PATTERN
    )

    description = validate_string_input(
        "Enter description: "
    )

    priority = validate_priority()

    task = Task(name, description, priority)
    tasks.append(task)

    save_tasks(tasks)
    print(f"Task '{name}' added successfully!")


def view_tasks(tasks):
    print("\n--- Your Current Tasks ---")

    if not tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(tasks, start=1):
        task.display(index)


def update_task(tasks):
    print("\n--- Update Task ---")

    if not tasks:
        print("No tasks found.")
        return

    view_tasks(tasks)

    index = validate_numeric_input(
        "Enter task number to update: "
    )

    if index > len(tasks):
        print("Invalid task number.")
        return

    task = tasks[index - 1]

    print("\nLeave a field blank to keep the existing value.")

    new_name = validate_string_input(
        f"New name [{task.name}]: ",
        pattern=TASK_NAME_PATTERN,
        allow_blank=True
    )

    new_description = validate_string_input(
        f"New description [{task.description}]: ",
        allow_blank=True
    )

    new_priority = input(
        f"New priority [{task.priority}] (High/Medium/Low): "
    ).strip()

    if new_name:
        task.name = new_name

    if new_description:
        task.description = new_description

    if new_priority:
        new_priority = new_priority.capitalize()

        if new_priority not in {"High", "Medium", "Low"}:
            print("Invalid priority. Please enter High, Medium, or Low.")
            return

        task.priority = new_priority

    save_tasks(tasks)
    print(f"Task '{task.name}' updated successfully!")


def delete_task(tasks):
    print("\n--- Delete Task ---")

    if not tasks:
        print("No tasks found.")
        return

    view_tasks(tasks)

    index = validate_numeric_input(
        "Enter task number to delete: "
    )

    if index > len(tasks):
        print("Invalid task number.")
        return

    task = tasks[index - 1]

    confirmed = validate_confirmation(
        f"Are you sure you want to delete '{task.name}'? (y/n): "
    )

    if not confirmed:
        print("Deletion cancelled.")
        return

    tasks.pop(index - 1)
    save_tasks(tasks)

    print(f"Task '{task.name}' deleted successfully!")


def main():
    tasks = load_tasks()

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            update_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
