import os
import time


FILE_PATH = "Tasks.txt"
tasks = []

def create_file():
    if not os.path.exists(FILE_PATH):
        try:
            with open(FILE_PATH, "w", encoding="utf-8"):
                print("File is created")
        except Exception:
            print("File cant created.")
            
            
def load_tasks():
    global tasks
    if os.path.exists(FILE_PATH):
        try:
            with open(FILE_PATH, "r", encoding="utf-8") as file:
                get_lines = file.readlines()
                if len(get_lines) > 0:
                    print("Tasks loading..."), time.sleep(2)
                    tasks = [line.rstrip("\n") for line in get_lines]
                    print(tasks)
                    print("Files loaded.")

        except FileNotFoundError:
            print("File not found.")
        
     
def save_tasks():
    global tasks
    if os.path.exists(FILE_PATH):
        print("Tasks saving..."), time.sleep(2)
        try:
            with open(FILE_PATH, "w", encoding="utf-8") as file:
                file.writelines(task + "\n" for task in tasks)
                print("Tasks saved...")
        except FileNotFoundError:
            print("File not found.")
    

def show_tasks():
    print("Searching current tasks..."), time.sleep(2)
    print("\n--|TASKS|--")
    print([f"{task}" for task in tasks]) if len(tasks) > 0 else print("The task list is empty")
    print("----------\n")

def insert_task():
    try:
        new_task = input("Enter the new task: ")
        if new_task != str(new_task): raise ValueError("Input cant be a number or empty value.")

        print("Inserting the new task...")
        
        num = int(input("Enter the task number: "))

        print("Inserting the task number...")
        time.sleep(2)
        if num != int(num): raise Exception("Error, these should be => a positive value, shouldn't be a string value, shouldn't be a empty value.")

        for task in tasks:
            
            if task.startswith(f"{num}- "): raise Exception("Error, there is another task with this number.")
            
            elif task.endswith(f"- {new_task}"): raise Exception("Error, this task already exists.")


            
        time.sleep(2), print("The new task is inserted.")
        print("Completed.")
        insert_the_task = str(num) + "- " + new_task
        tasks.append(insert_the_task)
        save_tasks()

    except ValueError as a:
        print(a)
    except Exception as b:
        print(b)

def delete_task():  
    try:
        show_tasks()
        num = int(input("Enter the task number: "))
        print("searching...")
        time.sleep(2)
        if num <= 0: raise ValueError("Invalid value, just enter a positive value.")

        for task in tasks[:]:

            if task.startswith(f"{num}- "):
                print(f"{task} is deleted from the list.")
                tasks.remove(task)
                save_tasks()
                break
            
        if not task.startswith(f"{num}- "): raise IndexError("That number cannot find in tasks.")

    except ValueError as a:
        print(a)
    except IndexError as e:
        print(e)

def edit_tasks():
    def sorting_key(sort_task):
        parts = sort_task.split('-', 1)
        if parts and parts[0].strip().isdigit():
            return int(parts[0].strip())
        return float('inf')
    
    global tasks
    show_tasks()
    request = input("[S]orting tasks list or [E]dit task?(Note: After editing, lists are sorted automatically): ").strip().lower()
    if request == "e":
        try:
            num = int(input("Enter the task number: ").strip())
            if not num or num <= 0: raise ValueError("Invalid number, negative value, empty value or string value.")
            
            print("Searching....") 
            time.sleep(2)
            found = False
            for index, task in enumerate(tasks):
                
                if task.startswith(f"{num}- "):
                    yeni_görev = input("New task: ").strip()
                    
                    if not yeni_görev: raise Exception("Input is cant be a empty value or integer value.")
                    
                    new_task = str(num) + "- " + yeni_görev
                    tasks[index] = new_task
                    found = True
                    print(f"{num}. task {'updated' if found else 'inserted.'}")
            
            if not found:
                cevap = input("No task, do you wanna insert this? ([Y]es/[N]o): ").strip().lower() == 'y'
                if cevap == "y":
                    tasks.append(new_task)
                elif cevap == "n": return 

            tasks = sorted(tasks, key=sorting_key)
            print("Files edited.")        
                      

        except ValueError as a:
            print(a)
        
        except Exception as e:
            print(e)

    elif request == "s":
        try:
            print("The task list sorting."), time.sleep(1)
            tasks = sorted(tasks, key=sorting_key)
            print("The task list sorted.")
            
        except Exception:
            print("Error, the list cant sorted.")

    save_tasks()
    show_tasks()

def ana_ekran():
    create_file()
    load_tasks()
    ekran = {
        'i': lambda: insert_task(),
        'd': lambda: delete_task(),
        's': lambda: show_tasks(),
        'e': lambda: edit_tasks(),
        'q': lambda: [print("Exiting..."), time.sleep(2), exit()]
    }
    
    while True:
        print("-------------------------------------")
        print("-----TASK MANAGEMENT APPLICATION-----")
        print("1- [I]nsert task.")
        print("2- [D]elete task.")
        print("3- [S]how the task list.")
        print("4- [E]dit the task from tasks list.")
        print("5- [Q]uit.")
        print("-------------------------------------")

        choice = input("Enter choice: ").lower()
        ekran.get(choice, lambda: [time.sleep(1), print("Invalid choice."), time.sleep(1)])() 

if __name__ == "__main__":     
    ana_ekran()