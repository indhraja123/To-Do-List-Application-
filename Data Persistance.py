def save_tasks(tasks, filename):
    with open(filename, 'w') as f:
        for task in tasks:
            f.write(task + '\n')

def load_tasks(filename):
    tasks = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass  # If the file doesn't exist yet, just return an empty list of tasks
    return tasks

def main():
    filename = 'tasks.txt'
    tasks = load_tasks(filename)
    
    while True:
        print("1. Add task")
        print("2. View tasks")
        print("3. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task = input("Enter task: ")
            tasks.append(task)
            save_tasks(tasks, filename)
        elif choice == '2':
            print("Tasks:")
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task}")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
