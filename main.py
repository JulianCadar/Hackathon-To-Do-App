import customtkinter as ctk
import AI
from functools import partial

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 800

class Task():
    def __init__(self, title: str,taskWidget):
        self.title = title
        self.completed =False
        self.taskWidget = taskWidget
        self.taskCheckBox = None
        self.MainTitle = None
        self.originalText = None

tasksToDo: list[Task] = []
completedTasks: list[Task] = []

def writeErrorMessage(msg):
    label = ctk.CTkLabel(master=window,text = msg,text_color="white")
    label.place(x=WINDOW_WIDTH/2, y=WINDOW_HEIGHT-50)
def addTask(tasks, taskTitle):
    #taskFrame = ctk.CTkFrame(master = frame, border_width=1, border_color="black")
    #taskFrame.grid_rowconfigure()
    #taskFrame.pack(side="top", fill="both", expand=True)
    if len(taskTitle)==0:
        writeErrorMessage("Too Short")
    
    else:
        summarizedTitle = AI.get_title(taskTitle)
        taskLabel = ctk.CTkLabel(master = frame, text = "    "+summarizedTitle +"    ",border_width=3,border_color="black",fg_color="white", text_color="black",bg_color="black")
        
        currentTaskWidget = Task(taskTitle,taskLabel)
        currentTaskWidget.originalText = taskTitle

        openDescButton = ctk.CTkButton(master= frame, text="Get Description",fg_color="white", text_color="black", command =lambda :partial(openDescFunction, currentTaskWidget)(),hover_color="light gray")
        openDescButton.grid(row=len(tasks), column=2, sticky="W")

        openGuideButton = ctk.CTkButton(master= frame, text="Get Guide",fg_color="white", text_color="black", command =lambda :partial(openGuideFunction, currentTaskWidget)(),hover_color="light gray")
        openGuideButton.grid(row=len(tasks), column=3, sticky="W")
        
        taskEntry.delete(1.0,ctk.END)
        #taskWidget.pack(side = "left")
        taskLabel.grid(row=len(tasks), column=0, sticky="W")

        taskCheckBox = ctk.CTkCheckBox(master = frame, text = "Completed?    ", command=lambda :partial(completedCheckBoxCallBack, currentTaskWidget)())
        #taskCheckBox.pack(side="right")
        taskCheckBox.grid(row=len(tasks), column=1, sticky="E")
        currentTaskWidget.taskCheckBox = taskCheckBox
        tasks.append(currentTaskWidget)


    
def completedCheckBoxCallBack(currentTaskWidget: Task):
    if (currentTaskWidget.taskCheckBox.get()):
        currentTaskWidget.taskWidget.destroy()
        currentTaskWidget.taskCheckBox.destroy()
        currentTaskWidget.completed=True
        

    return True

def openDescFunction(task:Task):
    originalTextWidget.configure(state="normal")
    originalTextWidget.delete(0.0, ctk.END)
    originalTextWidget.insert(0.0, task.originalText)

    originalTextWidget.configure(state="disabled")
def openGuideFunction(task:Task):
    originalTextWidget.configure(state="normal")
    originalTextWidget.delete(0.0, ctk.END)
    originalTextWidget.insert(0.0, AI.get_guide(task.originalText))

    originalTextWidget.configure(state="disabled")

window = ctk.CTk()
window.title("To Do App")
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
toDoLabel = ctk.CTkLabel(master = window, text = "To Do:", text_color="White",font = ("Arial",40))
toDoLabel.place(x=WINDOW_WIDTH/2 -600, y=WINDOW_HEIGHT/8 -50)
frame = ctk.CTkScrollableFrame(master = window, width = 600, height = 400)
frame.place(x = WINDOW_WIDTH/2 -600, y = WINDOW_HEIGHT/8)

taskEntry = ctk.CTkTextbox(master=window, width =300, height = 50)
taskEntry.place(x=WINDOW_WIDTH/2 -600, y = WINDOW_HEIGHT/8 -100)

taskAddButton = ctk.CTkButton(master = window, width = 100, height = 50, fg_color="white", text_color="black", text= "Add Task", border_color="black",border_width=2, hover_color="light gray",command = lambda :addTask(tasksToDo, taskEntry.get(1.0,ctk.END).strip()))
taskAddButton.place(x= WINDOW_WIDTH/2 -275, y = WINDOW_HEIGHT/8 -100)

descriptionFrame = ctk.CTkFrame(master=window, width =400, height = 400)
descriptionFrame.place(x = WINDOW_WIDTH/2, y = WINDOW_HEIGHT/8 -50)

descriptionLabel = ctk.CTkLabel(master = descriptionFrame, text = "Info: ", text_color="White",font = ("Arial",40))
#descriptionLabel.place(x=WINDOW_WIDTH/2, y=WINDOW_HEIGHT/8 -50)
descriptionLabel.pack(side="top")

#descriptionFrame = ctk.CTkScrollableFrame(master=window, width =400, height = 400)
#descriptionFrame.place(x = WINDOW_WIDTH/2, y = WINDOW_HEIGHT/8)



originalTextWidget = ctk.CTkTextbox(master=descriptionFrame, state="disabled", wrap="word")
originalTextWidget.pack(side="bottom")
window.mainloop()