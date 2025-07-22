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

def search():
    searchType = gui.buttonbox(choices=["Task names","Members"],
                                msg="Please enter what you want to search.")
    if searchType == "Task names":
        searchTerms = gui.enterbox("Please enter the task's name or ID:")
        found = False
        for taskID in tasks:
            if searchTerms is None or len(searchTerms) == 0:
                gui.msgbox(msg="Please enter a valid string...")
                found = True
                break

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
                            f"{tasks[taskID]['                  assignee']}")
                found = True
                break
        if found == False:
            gui.msgbox("Task not found.")

    elif searchType == "Members":
        searchTerms = gui.enterbox("Please enter the member's name or ID")
        for userID in users:
            if searchTerms is None:
                break

            elif searchTerms.lower() == userID.lower():
                gui.msgbox(msg=f'Found user with the ID: "{searchTerms}"\n\n'\
                            f"Name: {users[userID]['name']}\nEmail:" \
                            f"{users[userID]['email']}")
                found = True
                break

            elif searchTerms.lower() == users[userID]["name"].lower():
                gui.msgbox(msg=f'Found user with the name: "{searchTerms}"\n\n'\
                            f"Name: {users[userID]['name']}\nEmail:" \
                            f"{users[userID]['email']}")
                found = True
                break
            elif len(searchTerms) == 0:
                gui.msgbox(msg="Please enter a valid string...")
                found = True
                break
            
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
        elif int(priority)>3 or int(priority)<1:
            gui.msgbox("Priority must be between 1 or 3", "Error")
            continue
        elif status.lower() not in ["in progress",  "blocked",  "not started",  "finished"]:
            gui.msgbox(f"Status must be either not started, blocked, in Progress, or finished, current status = {status}")
            continue
        elif assignee.upper() not in users:
            gui.msgbox(f"Please enter a valid team member{[user for user in users]}. Current team member = {assignee}")
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
            "assignee":assignee.upper()
            }
        return

def listTasks():
    taskDetails = ""
    for task in tasks:
        taskDetails += f"------\nTitle: {tasks[task]['title']}\nDescription:" \
                           f"{tasks[task]['description']}\nPriority:"\
                           f"{tasks[task]['priority']}\nStatus:"\
                           f"{tasks[task]['status']}\nAssignee:"\
                           f"{tasks[task]['assignee']}\n"
    gui.msgbox(taskDetails)

def report():
    title = "Task manager"
    msg = "Select the task you want a report on:"

    taskNames = [tasks[task]["title"] for task in tasks]
    choice = gui.choicebox(msg, title, taskNames)
    for taskID in tasks:
        if tasks[taskID]["title"] == choice:
            gui.msgbox(title=tasks[taskID]['title'], 
                       msg=f"Title: {tasks[taskID]['title']}\nPriority:"\
                           f"{tasks[taskID]['priority']}\nStatus:"\
                           f"{tasks[taskID]['status']}\nAssignee:"\
                           f"{tasks[taskID]['assignee']}")

    if choice is None:
        return

#add val for status, has to be a member either code or full name, add val for search, show total task overview for report

def startUp():
    while True:
        choices = ["List task",
                   "New task",
                   "Search",
                   "Update task",
                   "Generate report", 
                   "Exit"
                   ]
        init = gui.buttonbox(
            "Welcome to [Generic Task Manager], " \
            "what would you like to do today?","Task manager",
            choices
            )
        if init == "List task":
            listTasks()
        elif init == "New task":
            newTask()
        elif init == "Search":
            search()
        elif init == "Update task":
            updateTask()
        elif init == "Generate report":
            report()
        elif init == "Exit":
            exit()
        elif init is None:
            exit()
        
startUp()