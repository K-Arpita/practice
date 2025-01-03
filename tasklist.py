#  Create a console application for basic CRUD operations on a list of tasks.

# Objective: Implement Create, Read, Update, and Delete operations using arrays or lists for data storage.



class Task:
    def __init__(self, task_id, task_name, task_description):
        self.task_id = task_id
        self.task_name = task_name
        self.task_description = task_description

    def __str__(self):
        return f"Task ID: {self.task_id}, Name: {self.task_name}, Description: {self.task_description}"

class TaskManager:
    def __init__(self):
        self.tasks = []  # List to store tasks
        self.next_id = 1  # Task ID counter

    # Create a new task
    def create_task(self):
        task_name = input("Enter task name: ")
        task_description = input("Enter task description: ")
        task = Task(self.next_id, task_name, task_description)
        self.tasks.append(task)
        self.next_id += 1
        print(f"Task '{task_name}' created successfully.")


    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task)

   
    def update_task(self):
        task_id = int(input("Enter task ID to update: "))
        task = self.find_task_by_id(task_id)
        if task:
            new_name = input(f"Enter new name for task (current: {task.task_name}): ")
            new_description = input(f"Enter new description for task (current: {task.task_description}): ")
            task.task_name = new_name
            task.task_description = new_description
            print(f"Task {task_id} updated successfully.")
        else:
            print(f"Task with ID {task_id} not found.")

    # Delete a task
    def delete_task(self):
        task_id = int(input("Enter task ID to delete: "))
        task = self.find_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            print(f"Task {task_id} deleted successfully.")
        else:
            print(f"Task with ID {task_id} not found.")

 
    def find_task_by_id(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

  
    def menu(self):
        while True:
            print("\nTask Manager Menu")
            print("1. Create Task")
            print("2. View Tasks")
            print("3. Update Task")
            print("4. Delete Task")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == '1':
                self.create_task()
            elif choice == '2':
                self.display_tasks()
            elif choice == '3':
                self.update_task()
            elif choice == '4':
                self.delete_task()
            elif choice == '5':
                print("Exiting Task Manager.")
                break
            else:
                print("Invalid option, please try again.")

# Create an instance of TaskManager and run the application
if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.menu()
