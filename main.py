import click

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
while True:
    
    if input() == "t":
        create_new_task()
    
    if input() == "p":
        print(tasksarray)


    if input() == "x":
        break
