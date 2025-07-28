from colorama import init, Fore, Style
from defs import *

init(autoreset=True)

while True:
    print(Fore.WHITE + Style.BRIGHT + "WELCOME TO TASK TRACKER CLI! WHAT WOULD YOU LIKE TO DO?")
    print(Fore.YELLOW + "1. Add a new task")
    print(Fore.YELLOW + "2. View all tasks")
    print(Fore.YELLOW + "3. Mark a task as completed")
    print(Fore.YELLOW + "4. Delete a task")
    print(Fore.RED + "5. Exit")

    choice = input(Fore.GREEN + "Please enter your choice [1-5]: ").strip()

    match choice:
        case "1":
            add_task()
        case "2":
            view_task()
        case "3":
            complete_task()
        case "4":
            delete_task()   
        case "5":
            break
        case _:
            print(Fore.RED + "Invalid option! Please try again by entering a valid option [1-5]")
        