from datetime import datetime

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
