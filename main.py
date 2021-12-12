import click

taskcounter = 0

#Create a new task
def newtask(): 
    input("Task: ")
    taskcounter = taskcounter +1  #I want to add +1 to the task counter but can´t
    print("You have ", taskcounter,"tasks")


#Main interface
print("Welcome to tasks")
print("Press t to create a new task")


answer = input()


if answer == "t":
    newtask()