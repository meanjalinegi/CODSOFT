Tasks=[]

def addtask():
    task= input("Enter a task you want to add in to do list: ")
    Tasks.append(task)
    print("Your task ",task," added to the list.")

def deletetask():
    listtask()
    try:
        tasktodelete =int(input("Enter a task you want to delete from to do list: "))
        if 0 <= tasktodelete < len(Tasks):
            Tasks.pop(tasktodelete)
            print("Task ",tasktodelete," has been removed.")
        else:
            print("Task ", tasktodelete, " not found")
    except:
        print("Invalid input.")

def listtask():
    if not Tasks:
        print("Your list is empty!!")
    else:
        print("Updated Tasks are : ")
        for index, task in enumerate(Tasks):
            print(f"Task#{index}. {task}")


#create a loop to run the app
print("Hey It's a To Do List app :)")
while True:
    print("\n")
    print("Create your To Do List")
    print("Please select one of the following options")
    print("__________________________________________")
    print("1. Add a new task")
    print("2. Delete a task")
    print("3. List task")
    print("4. Quit")

    choice = input("Enter your choice : ")

    if choice == "1":
        addtask()
    elif choice == "2":
        deletetask()
    elif choice == "3":
        listtask()
    elif choice == "4":
        break;
    else:
        print("Invalid input. please try again.")

print("Good bye:)")