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
        "status": "In Progress"
    },
    "T2": {
        "title" : "Implement Login page",
        "description": "Create the Login page for the website",
        "priority": 3,
        "status": "Blocked"
    },
    "T3": {
        "title" : "Fix navigation menu",
        "description": "Fix the navigation menu to be more user-friendly",
        "priority": 1,
        "status": "Not Started"
    },
    "T4": {
        "title" : "Add payment processing",
        "description": "Implement payment processing for the website",
        "priority": 2,
        "status": "In Progress"
    },
    "T5": {
        "title" : "Create an About Us page",
        "description": "Create a page with information about the company",
        "priority": 1,
        "status": "Blocked"
    },
}

def newTask():
    pass

def searchTask():
    pass
# search by name or ID

def updateTask():
    pass

def newTask(tasks):
    while True:
        fields = ["Title", "Description","Priority","Status"]
        info = gui.multenterbox("Please enter task details","Add new tasks", fields)
        if info is None:
            return
        title, desc, priority, status = info[0].strip(),info[1],info[2],info[3]
        if not title or not desc or not priority or not status:
            gui.msgbox("Please enter all values", "Error")
            continue
        if title in tasks:
            gui.msgbox("Title already exists", "Error")
            continue
        ID = tasks["T"+ str(len(tasks)+1)]
        tasks["T5"] = {"title":title, "description":desc, "priority":priority, "status":status}

def startUp():
    title  ="Task manager"
    msg = "Select your task:"

    for i in tasks:
        taskNames = [tasks[i]["title"] for i in tasks]
    choice = gui.choicebox(msg, title, taskNames)

newTask(tasks)