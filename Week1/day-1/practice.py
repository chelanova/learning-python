#exercise
## TODO: Create a Task Manager class
# Methods: add_task(), complete_task(), show_task(), show_pending
from datetime import datetime
class TaskManager:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, title, priority="medium"):
        task = {
            "id" : len(self.tasks) + 1,
            "title" : title,
            "priority" : priority,
            "completed" : False,
            "creted at" : datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        
        self.tasks.append(task)
        return f"Tasks added {title}"
    
    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                return f"Task {task_id} marked as complete!"
        return "Task not found"
    
    def show_tasks(self):
        if not self.tasks:
            print("No tasks yet!")
            return
        
        print("\n=== YOUR TASKS ===")
        for task in self.tasks:
            status = "✓" if task["completed"] else "○"
            print(f"{status} [{task['id']}] {task['title']} - Priority: {task['priority']}")
        print()
        
    def show_pending(self):
        pending = [t for t in self.tasks if not t["completed"]]
        print(f"\nPending task: {len(pending)}")
        for task in pending:
            print(f"  - {task['title']}")
        print()
        
        
tm = TaskManager()
tm.add_task("Learn Python OOP", "high")
tm.add_task("Build mini project", "high")
tm.add_task("Exercise", "low")
tm.show_tasks()
tm.complete_task(1)
tm.show_tasks()
tm.show_pending()