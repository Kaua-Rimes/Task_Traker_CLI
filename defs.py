import json
import os
from datetime import datetime
from colorama import init, Fore
from utils import *

data = []

def add_task():
    if os.path.exists("tasks_data.json"):
        with open ("tasks_data.json", "r") as tasks_data:
            data = json.load(tasks_data)
    else:
        data = []

    name = valid_text_input("Task name: ")
    description = valid_text_input("Task description: ")

    task = {
        "id": int(len(data) + 1),
        "name": name,
        "description": description,
        "created_at": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "completed" : False
    }
    data.append(task)

    try:
        with open("tasks_data.json", "w") as tasks_data:
            json.dump(data, tasks_data, indent=4)
    except FileNotFoundError:
        print(Fore.RED + "ERROR! Tasks file not found.")
    except json.JSONDecodeError:
        print(Fore.RED + "ERROR! File corrupted.")


def view_task():
    try:
        with open("tasks_data.json", "r") as file:
            tasks_data = json.load(file)
        
        for task in tasks_data:
            print(f"ID: {task['id']}")
            print(f"Name: {task['name']}")
            print(f"Description: {task['description']}")
            print(f"Created at: {task['created_at']}")
            if task['completed']:
                print(Fore.GREEN + "Completed")
            else:
                print(Fore.YELLOW + "In Progress")

    except FileNotFoundError:
        print(Fore.RED + "ERROR! Tasks file not found.")
    except json.JSONDecodeError:
        print(Fore.RED + "ERROR! File corrupted.")


def complete_task():
    global data

    if not data:
        if os.path.exists("tasks_data.json"):
            try:
                with open("tasks_data.json", "r") as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                print(Fore.RED + "ERROR! File corrupted.")
                return
        else:
            print(Fore.RED + "No tasks available.")
            return

    if not data:
        print(Fore.RED + "No tasks available.")
        return

    while True:
        try:
            choose_option = int(input("What is the ID of the task you would like to mark as completed? "))
            
            task_ids = [task["id"] for task in data]
            if choose_option not in task_ids:
                print(Fore.RED + "ERROR! Insert a valid ID number.")
            else:
                break
        except ValueError:
            print(Fore.RED + "ERROR! Insert a valid ID number.")

    for task in data:
        if task["id"] == choose_option:
            task["completed"] = True
            print(Fore.GREEN + f"Task {choose_option} marked as completed.")
            break

    try:
        with open("tasks_data.json", "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(Fore.RED + f"ERROR! Could not save tasks: {e}")

    


