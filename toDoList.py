class colors:
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'
 
    class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'
 
    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'

def printCritical(text):
    print(colors.bg.black, colors.fg.red)
    print(text, colors.reset)

def printWarning(text):
    print(colors.bg.black, colors.fg.orange)
    print(text, colors.reset)

def printSuccess(text):
    print(colors.bg.black, colors.fg.green)
    print(text, colors.reset)

def printWorking(text):
    print(colors.bg.black, colors.fg.blue)
    print(text, colors.reset)

def askMenu(choices, text):
    counter = 1
    choice_list = []
    for choice in choices:
        new_choice = str(counter) + ". " + choice
        choice_list.append(new_choice) 
        counter += 1
    separator = "\n"
    menu = separator.join(choice_list)
    printWorking(menu)
    printWarning(text)
    user_input = input("Selection: ")
    try:
        index = int(user_input)
        index <= len(choices) == True
        index >= 0 == True
    except ValueError:
        printCritical("Please make sure choose one of the chosen options!")
    except TypeError:
        printCritical("Please make sure to input numbers for menu selections!")
    else:
        return index-1

def addTask(list, task):
    new_list = list
    new_list.append(task)
    print("Task added!")
    return new_list
    
def viewTasks(list):
    counter = 1
    tasks = []
    for task in list:
        concat = str(counter) + ". " + str(task[0]) + " - " + str(task[1]) + " - " + str(task[2])
        tasks.append(concat)
        counter += 1
    separator = "\n"
    string = separator.join(tasks)
    print(string)

def updateTask(list, choice, task):
    new_list = list
    new_list[choice] = task
    print("Updated task!")
    return new_list

def deleteTask(list, choice):
    new_list = list
    del new_list[choice]
    return new_list

def mainLoop():
    task_list = []
    while True:
        printSuccess("Welcome to the To-Do List App!")
        # grabbing selection from main menu
        input_option = askMenu(["Add a task", "View tasks", "Update task", "Delete a task"], "Please select an option:")
        try:
            printWorking("Working...")
            #validation of inputs
            option = int(input_option)
            # if input doesn't throw error, check which option was selected and try to set up what will be passed to the function later
            if option == 0:
                input_text = str(input("Task name: "))
                input_priority = askMenu(["High", "Medium", "Low"], "Please select a priority for this task:")
                # here I check what choice index was chosen, then overwriting the same variable with the string I want for later
                if input_priority == 0:
                    input_priority = "High"
                if input_priority == 1:
                    input_priority = "Medium"
                if input_priority == 2:
                    input_priority = "Low"
                # this is all scoped together so I can just declare this here and pick it up later for a function. scary, but neat!
                task = [input_text, "incomplete", input_priority]
            elif option == 2:
                # showing the list of tasks properly requires a bit of extra work since I want to display a list of lists
                # I have to unpack and concat each saved task to give the askMenu function for it to look right
                choices = []
                for task in task_list:
                    choices.append(task[0] + " - " + task[1] + " - " + task[2])
                task_choice = askMenu(choices, "Please select the task to update:")
                old_task = task_list[task_choice]
                input_operation = askMenu(["Name", "Status", "Priority"], "Please select what you would like to update:")
                if input_operation == 0:
                    text = str(input("New name: "))
                    old_task[0] = text
                elif input_operation == 1:
                    input_status = askMenu(["Complete", "Incomplete"], "Please select a status for this task:")
                    if input_status == 0:
                        input_status = "Complete"
                    if input_status == 1:
                        input_status = "Incomplete"
                    old_task[1] = input_status
                elif input_operation == 2:
                    input_priority = askMenu(["High", "Medium", "Low"], "Please select a priority for this task:")
                    if input_priority == 0:
                        input_priority = "High"
                    if input_priority == 1:
                        input_priority = "Medium"
                    if input_priority == 2:
                        input_priority = "Low"
                    old_task[2] = input_priority
            elif option == 3:
                # same thing as before since I'm displaying a list of lists. If all of this works well, I'll just pick up the variables later in the else block and do the desired operation.
                choices = []
                for task in task_list:
                    choices.append(task[0] + " - " + task[1] + " - " + task[2])
                task_choice = askMenu(choices, "Please select the task to delete:")
        except ValueError:
            printCritical("Please make sure choose one of the chosen options!")
        except TypeError:
            printCritical("Please make sure to input numbers for menu selections!")
        except:
            printCritical("An unknown error has occured. Double check any inputs and try again!")
        else:
            #do operations here
            if option == 0:
                task_list = addTask(task_list, task)
            if option == 1:
                viewTasks(task_list)
            if option == 2:
                task_list = updateTask(task_list, task_choice, old_task)
            if option == 3:
                task_list = deleteTask(task_list, task_choice)
        finally:
            printSuccess("done!\n------------------------------")
            

mainLoop()

