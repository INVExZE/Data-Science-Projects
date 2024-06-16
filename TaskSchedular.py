from datetime import datetime

def log_action(action):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            print(f"{action} task: {self.description}, Deadline: {self.deadline.strftime('%Y-%m-%d %H:%M:%S')}")
            return result
        return wrapper
    return decorator

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    @log_action("Added")
    def add_task(self):
        pass

    @log_action("Completed")
    def complete_task(self):
        self.completed = True

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)
        task.add_task()

    def complete_task(self, description):
        for task in self.tasks:
            if task.description == description and not task.completed:
                task.complete_task()
                return True
        return False

    def display_tasks(self):
        for task in self.tasks:
            status = "Completed" if task.completed else "Pending"
            print(f"Task: {task.description}, Deadline: {task.deadline.strftime('%Y-%m-%d %H:%M:%S')}, Status: {status}")

# Example usage
scheduler = TaskScheduler()

# Adding tasks
scheduler.add_task("Buy groceries", datetime(2024, 5, 28, 17, 0))
scheduler.add_task("Finish report", datetime(2024, 5, 27, 23, 59))

# Displaying all tasks
print("All tasks:")
scheduler.display_tasks()

# Completing a task
scheduler.complete_task("Buy groceries")

# Displaying all tasks after completing one
print("\nTasks after completion:")
scheduler.display_tasks()
