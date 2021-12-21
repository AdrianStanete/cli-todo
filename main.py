

taskcounter = 0
tasksarray = []

def print_main_interface():
    print("Welcome to this shiny to-do app. What do you want to do?")
    print("t to create a new task")
    print("p to print your tasks")
    print("x to exit")

def create_new_task(): 
    task = input("Task: ")
    tasksarray.append(task)
    taskcounter = +1  

print_main_interface()
option = input("Choose an option: ")

while option != "x":
    
    if option == "t":
        create_new_task()
    
    elif option == "p":
        print(tasksarray)
    else:
        print("Invalid option.")

    print_main_interface()
    option = input("Choose an option: ")

print("Thanks for using the app")
