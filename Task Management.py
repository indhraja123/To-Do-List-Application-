import json
import os
from datetime import datetime

# File to store tasks
TASKS_FILE = "tasks.json"

# Load tasks from file if it exists
tasks = []
if os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, 'r') as file:
        tasks = json.load(file)

def save_tasks():
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task():
    title = input("Enter task title: ")
    priority = input("Enter priority (high/medium/low): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")

    tasks.append({
        "title": title,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    })

    save_tasks()
    print("Task added successfully.")

def remove_task():
    list_tasks()
    index = int(input("Enter the index of the task to remove: "))
    if 0 <= index < len(tasks):
        del tasks[index]
        save_tasks()
        print("Task removed successfully.")
    else:
        print("Invalid task index.")

def mark_completed():
    list_tasks()
    index = int(input("Enter the index of the task to mark as completed: "))
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks()
        print("Task marked as completed.")
    else:
        print("Invalid task index.")

def list_tasks():
    print("Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i}. {task['title']} - Priority: {task['priority']} - Due Date: {task['due_date']} - Completed: {'Yes' if task['completed'] else 'No'}")

# Main loop
while True:
    print("\n1. Add Task\n2. Remove Task\n3. Mark Task as Completed\n4. List Tasks\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        remove_task()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        list_tasks()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
