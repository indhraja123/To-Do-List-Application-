class Task:
    def _init_(self, name, priority):
        self.name = name
        self.priority = priority

class TaskManager:
    def _init_(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_tasks_by_priority(self, priority):
        return [task for task in self.tasks if task.priority == priority]

# Example usage:
task_manager = TaskManager()

task1 = Task("Complete project", "high")
task2 = Task("Buy groceries", "medium")
task3 = Task("Read book", "low")

task_manager.add_task(task1)
task_manager.add_task(task2)
task_manager.add_task(task3)

high_priority_tasks = task_manager.get_tasks_by_priority("high")
print("High priority tasks:")
for task in high_priority_tasks:
    print(task.name)

medium_priority_tasks = task_manager.get_tasks_by_priority("medium")
print("\nMedium priority tasks:")
for task in medium_priority_tasks:
    print(task.name)

low_priority_tasks = task_manager.get_tasks_by_priority("low")
print("\nLow priority tasks:")
for task in low_priority_tasks:
    print(task.name)
