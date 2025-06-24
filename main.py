#Imports
import easygui as gui

#Data
users = {
    "JSM": {
        "name": "John Smith",
        "email": "John@techvision.com",
        "password": "WWR"
    },
    "JLO":{
        "name": "Jane Love",
        "email": "John@techvision.com",
         "password": "Loober"
    },
    "BDI":{
        "name": "Bob Dillon",
        "email": "Bob@techvision.com",
         "password": "Lupis"
    }
}

tasks = {
    "T1": {
        "title" : "Design Homepage",
        "description": "Create a mockup of the homepage",
        "priority": 3,
        "status": "In Progress",
        "assignee": "JSM"
    },
    "T2": {
        "title" : "Implement Login page",
        "description": "Create the Login page for the website",
        "priority": 3,
        "status": "Blocked",
        "assignee": "JLO"
    },
    "T3": {
        "title" : "Fix navigation menu",
        "description": "Fix the navigation menu to be more user-friendly",
        "priority": 1,
        "status": "Not Started",
        "assignee": "BDI"
    },
    "T4": {
        "title" : "Add payment processing",
        "description": "Implement payment processing for the website",
        "priority": 2,
        "status": "In Progress",
        "assignee": "BDI"
    },
    "T5": {
        "title" : "Create an About Us page",
        "description": "Create a page with information about the company",
        "priority": 1,
        "status": "Blocked",
        "assignee": "JSM"
    },
}

def searchTask():
    searchTerms = gui.enterbox("Please enter what you want to search")
    found = False
    for taskID in tasks:
        if searchTerms is None:
            return

        elif searchTerms.lower() == taskID.lower():
            gui.msgbox(msg=f'Found task with the ID: "{searchTerms}"\n\n'\
                           f"Title: {tasks[taskID]['title']}\nDescription:" \
                           f"{tasks[taskID]['description']}\nPriority:"\
                           f"{tasks[taskID]['priority']}\nStatus:"\
                           f"{tasks[taskID]['status']}\nAssignee:"\
                           f"{tasks[taskID]['assignee']}")
            found = True
            break

        elif searchTerms.lower() == tasks[taskID]["title"].lower():
            gui.msgbox(msg=f'Found task with the title: "{searchTerms}"\n\n'\
                           f"Title: {tasks[taskID]['title']}\nDescription:" \
                           f"{tasks[taskID]['description']}\nPriority:"\
                           f"{tasks[taskID]['priority']}\nStatus:"\
                           f"{tasks[taskID]['status']}\nAssignee:"\
                           f"{tasks[taskID]['assignee']}")
            found = True
            break
    if found == False:
        gui.msgbox("Task not found.")
        
def updateTask():
    title  ="Task manager"
    msg = "Select the task you want to update:"

    taskNames = [tasks[task]["title"] for task in tasks]
    edit = gui.choicebox(msg, title, taskNames)
    for taskID in tasks:
        if tasks[taskID]["title"] == edit:
            fields = ["Title", "Description","Priority","Status", "Assignee"]
            info = gui.multenterbox(
                "Please enter task's new details","update task",fields)
            if info is None:
                return
            title, desc, priority = info[0],info[1],info[2]
            status, assignee = info[3],info[4]
            if not title or not desc or not priority or not status or not assignee:
                gui.msgbox("Please enter all values", "Error")
                continue
            elif not priority.isdigit():
                gui.msgbox("Priority must be a positive whole number", "Error")
                continue
            elif title != tasks:
                gui.msgbox("Title doesn't exist yet, try creating a new task"\
                    " instead", "Error")
                continue
            taskID = f"T{str(len(tasks) + 1)}"
            tasks[taskID] = {
                "title":title, 
                "description":desc, 
                "priority":priority, 
                "status":status,
                "assignee":assignee
                }
            return

    if edit is None:
        return

def newTask():
    while True:
        fields = ["Title", "Description","Priority","Status", "Assignee"]
        info = gui.multenterbox(
            "Please enter task details","Add new tasks",
            fields
            )
        if info is None:
            return
        title, desc, priority = info[0],info[1],info[2]
        status, assignee = info[3],info[4]
        if not title or not desc or not priority or not status or not assignee:
            gui.msgbox("Please enter all values", "Error")
            continue
        elif not priority.isdigit():
            gui.msgbox("Priority must be a positive whole number", "Error")
            continue
        elif title in tasks:
            gui.msgbox("Title already exists", "Error")
            continue
        taskID = f"T{str(len(tasks) + 1)}"
        tasks[taskID] = {
            "title":title, 
            "description":desc, 
            "priority":priority, 
            "status":status,
            "assignee":assignee
            }
        return

def listTasks():
    title  ="Task manager"
    msg = "Select your task:"

    taskNames = [tasks[task]["title"] for task in tasks]
    choice = gui.choicebox(msg, title, taskNames)
    for taskID in tasks:
        if tasks[taskID]["title"] == choice:
            gui.msgbox(title=tasks[taskID]['title'], 
                       msg=f"Title: {tasks[taskID]['title']}\nDescription:" \
                           f"{tasks[taskID]['description']}\nPriority:"\
                           f"{tasks[taskID]['priority']}\nStatus:"\
                           f"{tasks[taskID]['status']}\nAssignee:"\
                           f"{tasks[taskID]['assignee']}")

    if choice is None:
        return

def startUp():
    while True:
        choices = ["List task","New task","Search task", "Update task", "Exit"]
        init = gui.buttonbox(
            "Welcome to [Generic Task Manager], " \
            "what would you like to do today?","Task manager",
            choices
            )
        if init == "List task":
            listTasks()
        elif init == "New task":
            newTask()
        elif init == "Search task":
            searchTask()
        elif init == "Update task":
            updateTask()
        elif init == "Exit":
            exit()
        elif init is None:
            exit()
        
startUp()