class Task:
    def __init__(self, name, description, status, column):
        self.name = name
        self.description = description
        self.status = status
        self.column = column
    def add_task(name, description, status):
    new_task = Task(name, description, status, "бэклог")
    tasks.append(new_task)
    def remove_task(task_name):
    for task in tasks:
        if task.name == task_name:
            tasks.remove(task)
            return True
    return False
    def move_to_work(task):
    task.column = "в работе"
    task.status = "не выполнено"

    def mark_as_done(task):
    task.column = "выполнено"
    task.status = "выполнено"
    def show_tasks():
    print("Список

