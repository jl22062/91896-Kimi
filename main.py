# Imports
import easygui as gui  # GUI pop-up library for quick inputs

# Data
tasks = {  # Stores all task info with ID as key
    "T1": {  # Task ID
        "title": "Design Homepage",  # Task name
        "description": "Create a mockup of the homepage",  # What needs doing
        "priority": 3,  # 1 = high, 3 = low
        "status": "In Progress",  # Current state of task
        "assignee": "JSM"  # Who's doing it
    },
    "T2": {
        "title": "Implement Login page",
        "description": "Create the Login page for the website",
        "priority": 3,
        "status": "Blocked",
        "assignee": "JLO"
    },
    "T3": {
        "title": "Fix navigation menu",
        "description": "Fix the navigation menu to be more user-friendly",
        "priority": 1,
        "status": "Not Started",
        "assignee": "BDI"
    },
    "T4": {
        "title": "Add payment processing",
        "description": "Implement payment processing for the website",
        "priority": 2,
        "status": "In Progress",
        "assignee": "BDI"
    },
    "T5": {
        "title": "Create an About Us page",
        "description": "Create a page with information about the company",
        "priority": 1,
        "status": "Blocked",
        "assignee": "JSM"
    },
}

users = {  # Stores all user info with ID as key
    "JSM": {
        "name": "John Smith",  # Full name
        "email": "John@techvision.com",  # Contact email
        "assigned": []  # Holds assigned task IDs
    },
    "JLO": {
        "name": "Jane Love",
        "email": "John@techvision.com",
        "assigned": []
    },
    "BDI": {
        "name": "Bob Dillon",
        "email": "Bob@techvision.com",
        "assigned": []
    }
}

# Search function
def search():
    """
    Lets the user search for either a task or a member
    and shows matches with partial search supported.
    """

    # Pick search type
    searchType = gui.buttonbox(choices=["Task names", "Members"],
                                msg="Please enter what you want to search.")
    # Search tasks
    if searchType == "Task names":
        searchTerms = gui.enterbox("Please enter the task's name or ID:")
        found = False
        # Reject empty
        if searchTerms is None or len(searchTerms.strip()) == 0:
            gui.msgbox(msg="Please enter a valid string...")
            return
        searchTerms = searchTerms.strip()
        for taskID in tasks:
            # Match by ID
            if searchTerms.lower() == taskID.lower():
                gui.msgbox(msg=f'Found task with the ID: "{searchTerms}"\n\n'
                               f"Title: {tasks[taskID]['title']}\nDescription: "
                               f"{tasks[taskID]['description']}\nPriority: "
                               f"{tasks[taskID]['priority']}\nStatus: "
                               f"{tasks[taskID]['status']}\nAssignee: "
                               f"{tasks[taskID]['assignee']}")
                found = True
                break
            # Match by title
            elif searchTerms.lower() in tasks[taskID]["title"].lower():
                gui.msgbox(msg=f'Found task with the title: "{searchTerms}"\n\n'
                               f"Title: {tasks[taskID]['title']}\nDescription: "
                               f"{tasks[taskID]['description']}\nPriority: "
                               f"{tasks[taskID]['priority']}\nStatus: "
                               f"{tasks[taskID]['status']}\nAssignee: "
                               f"{tasks[taskID]['assignee']}")
                found = True
                break
        if not found:
            gui.msgbox("Task not found.")
    # Search members
    elif searchType == "Members":
        searchTerms = gui.enterbox("Please enter the member's name or ID")
        found = False
        if searchTerms is None or len(searchTerms.strip()) == 0:
            gui.msgbox(msg="Please enter a valid string...")
            return
        searchTerms = searchTerms.strip()
        for userID in users:
            search = searchTerms.lower()
            # Match by ID or name
            if search in userID.lower() or search in users[userID]["name"].lower():
                # Build assigned task list
                for task_id, task_data in tasks.items():
                    assignee = task_data["assignee"]
                    if assignee in users:
                        users[assignee]["assigned"].append(task_id)
                # Show results
                gui.msgbox(msg=f'Found user: "{searchTerms}"\n\n'
                               f"Name: {users[userID]['name']}\nEmail: "
                               f"{users[userID]['email']}\nAssigned tasks: "
                               f"{users[userID]['assigned']}")
                # Clear assigned list after
                for task_id, task_data in tasks.items():
                    assignee = task_data["assignee"]
                    if assignee in users:
                        users[assignee]["assigned"].remove(task_id)
                found = True
                break
        if not found:
            gui.msgbox("User not found.")

# Update function         
def updateTask():
    # Show all task titles
    taskNames = [tasks[task]["title"] for task in tasks]
    taskSelected = gui.choicebox(
        msg="Select the task you want to update:", 
        title="Task manager", choices=taskNames
        )
    if not taskSelected:
        return
    # Find ID for selected task
    for taskID in tasks:
        if tasks[taskID]["title"] == taskSelected:
            IDSelected = taskID
    while True:
        # Pick field to edit
        fieldSelected = gui.choicebox(
            msg="Select what you want to edit:", 
            title="Task manager", choices=list(tasks[IDSelected].keys()))
        if fieldSelected is None:
            return
        # Get new value
        info = gui.enterbox(
            title="Task manager", 
            msg=f"Please enter the new value for {fieldSelected}"
            )
        if info is None:
            return
        info = info.strip()
        # Priority check
        if fieldSelected == "priority":
            if not info.isdigit() or not (1 <= int(info) <= 3):
                gui.msgbox("Priority must be a whole number between 1 and 3", "Error")
                continue
            else:
                tasks[IDSelected][fieldSelected] = int(info)
                return
        # Status check
        elif fieldSelected == "status":
            if info.lower() not in ["in progress", "blocked", "not started", "completed"]:
                gui.msgbox(
                    f"Status must be either Not Started, Blocked,"
                    f"In Progress, or Completed. Current = {info}"
                    )
                continue
            else:    
                tasks[IDSelected][fieldSelected] = info.title()
                return
        # Assignee check
        elif fieldSelected == "assignee":
            if info.upper() not in users:
                gui.msgbox(
                    f"Please enter a valid team member {list(users.keys())}. Current = {info}"
                    )
                continue
            else:
                tasks[IDSelected][fieldSelected] = info.upper()
                return

# New Task function
def newTask():
    info = []
    while True:
        # Prompt for all details
        fields = ["Title", "Description", "Priority", "Status", "Assignee"]
        info = gui.multenterbox("Please enter task details", "Add new tasks", fields, info)
        if info is None:
            return
        # Strip inputs
        title, desc, priority = info[0].strip(), info[1].strip(), info[2].strip()
        status, assignee = info[3].strip(), info[4].strip()
        # Check all filled
        if not title or not desc or not priority or not status or not assignee:
            gui.msgbox("Please enter all values", "Error")
            continue
        # Priority checks
        elif not priority.isdigit():
            gui.msgbox("Priority must be a positive whole number", "Error")
            continue
        elif int(priority) > 3 or int(priority) < 1:
            gui.msgbox("Priority must be between 1 or 3", "Error")
            continue
        # Status check
        elif status.lower() not in ["in progress", "blocked", "not started", "completed"]:
            gui.msgbox(
                f"Status must be either Not Started, Blocked,"
                f"In Progress, or Completed. Current = {status}"
                )
            continue
        # Assignee check
        elif assignee.upper() not in users:
            gui.msgbox(
                f"Please enter a valid team member {list(users.keys())}. Current = {assignee}"
                )
            continue
        # Title uniqueness
        elif title in [task["title"] for task in tasks.values()]:
            gui.msgbox("Title already exists", "Error")
            continue
        # Add task to dict
        taskID = f"T{str(len(tasks) + 1)}"
        tasks[taskID] = {
            "title": title,
            "description": desc,
            "priority": int(priority),
            "status": status.title(),
            "assignee": assignee.upper()
        }
        return

# Listing task function
def listTasks():
    taskDetails = ""  # Builds display string
    for task in tasks:
        taskDetails += f"------\nTitle: {tasks[task]['title']}\nDescription: " \
                       f"{tasks[task]['description']}\nPriority: " \
                       f"{tasks[task]['priority']}\nStatus: " \
                       f"{tasks[task]['status']}\nAssignee: " \
                       f"{tasks[task]['assignee']}\n"
    gui.msgbox(taskDetails)

# Report function
def report():
    # Counters for statuses
    completed, in_progress, blocked, not_started = 0, 0, 0, 0
    for task in tasks.values():
        if task["status"] == "Completed":
            completed += 1
        elif task["status"] == "In Progress":
            in_progress += 1
        elif task["status"] == "Blocked":
            blocked += 1
        elif task["status"] == "Not Started":
            not_started += 1
    # Show results
    gui.msgbox(f"--- Overall task report ---\n"
               f"Task completed: {completed}\n"
               f"Task in progress: {in_progress}\n"
               f"Task blocked: {blocked}\n"
               f"Task not started: {not_started}")

# Initial startup
def startUp():
    while True:
        # Main menu
        choices = ["List task",
                   "New task",
                   "Search",
                   "Update task",
                   "Generate report",
                   "Exit"
                   ]
        init = gui.buttonbox("Welcome to [Generic Task Manager], "
                             "what would you like to do today?", "Task manager", choices)
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
        elif init == "Exit" or init is None:
            exit()

# Runs the main start up function    
startUp()
