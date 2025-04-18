# This file is sketch for to-do cli app
# commands: 
# add <task name>: add task to list
# list : lists all tasks
# save : save tasks to file
# exit : terminate program

# datastructure
todos = {}


def load():
    # this feature will add in future
    # read the saved file if there is any and load todos
    with open('todos_list.txt', 'r') as file:
        pass

def save():
    # save the list to file
    with open('todos_list.txt', 'w') as file:
        pass

def add(task_name):
    # adds a task to todo list
    pass

def main():
    # main functionality of the program
    
    while True:
   
        input_command = input("Enter command: ")
        if not input_command:
            print("Empty command. type help for help.\n")
            continue

        parser = input_command.split()
        command = parser[0]

        if command == "add":
            print("Not implemented yet!")
            # task_name = " ".join(parser[1:])
            # add(task_name)
        
        elif command == "list":
            if len(todos) == 0:
                print("todo list is empty.\n")
            else:
                for idx, todo in todos.items():
                    print(f"{idx}.{todo}")

        elif command == "save":
            save()
        
        elif command == "exit":
            break
        
        elif command == "help":
            print("""
                commands: 
                    add <task-name1> <task-name2>:: add tasks to todo list
                    list :: list all tasks in todo
                    save :: save tasts to file
                    exit :: terminate the program
                    """)
        else:
            print("Type help for help.")

if __name__ == '__main__':
    main()