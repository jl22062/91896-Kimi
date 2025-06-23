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
    pass
# search by name or ID

def updateTask():
    pass

def newTask():
    while True:
        fields = ["Title", "Description","Priority","Status", "Assignee"]
        info = gui.multenterbox(
            "Please enter task details","Add new tasks",
            fields
            )
        if info is None:
            return
        title, desc, priority, status, assignee = info[0].strip(),info[1],info[2],info[3],info[4]
        if not title or not desc or not priority or not status or not assignee:
            gui.msgbox("Please enter all values", "Error")
            continue
        elif not priority.isdigit():
            gui.msgbox("Priority must be a positive whole number", "Error")
            continue
        elif title in tasks:
            gui.msgbox("Title already exists", "Error")
            continue
        taskID = "T" + str(len(tasks) + 1)
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
        choices = ["List task","New task","aP"]
        init = gui.buttonbox(
            "Welcome to [Generic Task Manager], " \
            "what would you like to do today?","Task manager",
            choices
            )
        if init == "List task":
            listTasks()
        elif init == "New task":
            newTask()
        elif init is None:
            exit()
        
startUp()