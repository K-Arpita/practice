#  Task 5: Enhance the CRUD application to store task data persistently using file I/O.

# Objective: Implement file storage for tasks  to enable saving and loading from a text file.


import os

# Function to read tasks from a file
def read_tasks_from_file(filename):
    tasks = []
    try:
        with open(filename, 'r') as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with an empty task list.")
    except IOError as e:
        print(f"Error reading the file: {e}")
    return tasks

# Function to write tasks to a file
def write_tasks_to_file(filename, tasks):
    try:
        with open(filename, 'w') as file:
            for task in tasks:
                file.write(task + '\n')
    except IOError as e:
        print(f"Error writing to file: {e}")

# Function to add a new task
def add_task(task, tasks):
    tasks.append(task)
    print(f"Task '{task}' added.")
    return tasks

# Function to display all tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
    else:
        print("Task List:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")

# Function to delete a task
def delete_task(task_index, tasks):
    try:
        removed_task = tasks.pop(task_index - 1)
        print(f"Task '{removed_task}' removed.")
    except IndexError:
        print("Invalid task index.")

# Main function to run the CRUD application
def task_manager(filename="task.txt"):
    tasks = read_tasks_from_file(filename)

    while True:
        print("\nTask Manager:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter you choice: ")

        if choice == '1':
            task = input("Enter task: ")
            tasks = add_task(task, tasks)
            write_tasks_to_file(filename, tasks)
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            task_index = int(input("Enter task number to delete: "))
            delete_task(task_index, tasks)
            write_tasks_to_file(filename, tasks)
        elif choice == '4':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the Task Manager
task_manager()
