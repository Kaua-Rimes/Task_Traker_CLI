import json
import os
from datetime import datetime

data = []

def add_task():
    if os.path.exists("tasks_data.json"):
        with open ("tasks_data.json", "r") as tasks_data:
            data = json.load(tasks_data)
    else:
        data = []

    task = {
        "id": len(data) + 1,
        "name": input("Task name: "),
        "description": input("Task description: "),
        "created_at": datetime.now().strftime("%d/%m/%Y %H:%M")
    }
    data.append(task)

    with open("tasks_data.json", "w") as tasks_data:
        json.dump(data, tasks_data, indent=4)


def view_task():
    with open ("tasks_data.json", "r") as file:
        task = json.load(file)
        
        for task in task:
            print(f"ID: {task['id']}")
            print(f"Name: {task['name']}")
            print(f"Description: {task['description']}")
            print(f"Created at: {task['created_at']}")
            print("-" * 20)
    


