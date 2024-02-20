[2:56 PM, 2/20/2024] Indhu❤️: from datetime import datetime

class Task:
    def _init_(self, name, due_date=None):
        self.name = name
        self.due_date = due_date

    def set_due_date(self, due_date):
        self.due_date = due_date

    def get_due_date(self):
        return self.due_date

def create_task():
    name = input("Enter task name: ")
    due_date_str = input("Enter due date (YYYY-MM-DD): ")
    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return None
    return Task(name, due_date)

def main():
    tasks = []

    while True:
        print("\n1. Create Task")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = create_task()
            if task:
                tasks.append(task)
                print("Task created successfully.")
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please try again.")

    print("\nTasks:")
    for task in tasks:
        print(f"{task.name} - Due Date: {task.get_due_date().strftime('%Y-%m-%d') if task.get_due_date() else 'Not set'}")

if _name_ == "_main_":
    main()
[3:05 PM, 2/20/2024] Indhu❤️: class Task:
    def _init_(self, name, priority='medium', due_date=None):
        self.name = name
        self.priority = priority
        self.completed = False
        self.due_date = due_date

class TaskManager:
    def _init_(self):
        self.tasks = []

    def add_task(self, name, priority='medium', due_date=None):
        new_task = Task(name, priority, due_date)
        self.tasks.append(new_task)

    def remove_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)

    def mark_as_completed(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True

    def display_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. Name: {task.name}, Priority: {task.priority}, Due Date: {task.due_date}, Completed: {task.completed}")

# Example usage:
task_manager = TaskManager()

task_manager.add_task("Complete project", priority="high", due_date="2024-03-15")
task_manager.add_task("Study for exam", priority="medium", due_date="2024-02-25")
task_manager.add_task("Buy groceries", priority="low")

task_manager.display_tasks()

task_manager.mark_as_completed("Study for exam")
task_manager.remove_task("Buy groceries")

print("\nAfter marking 'Study for exam' as completed and removing 'Buy groceries':")
task_manager.display_tasks()
