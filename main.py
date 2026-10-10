import customtkinter as ctk
import openai
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 800
class Task():
    def __init__(self, title: str, completed:bool):
        self.title = title
        self.completed = completed
tasks:list[Task] = []
def writeErrorMessage(msg):
    label = ctk.CTkLabel(master=window,text = msg,text_color="white")
    label.place(x=WINDOW_WIDTH/2, y=WINDOW_HEIGHT-50)
def addTask():
    #taskFrame = ctk.CTkFrame(master = frame, border_width=1, border_color="black")
    #taskFrame.grid_rowconfigure()
    #taskFrame.pack(side="top", fill="both", expand=True)
    taskTitle = taskEntry.get(1.0,ctk.END).strip()
    if len(taskTitle)==0:
        writeErrorMessage("Too Short")
    elif len(taskTitle)>49:
        writeErrorMessage("Too long")
        taskEntry.delete(1.0,ctk.END)
    else:
        taskWidget = ctk.CTkLabel(master = frame, text = taskTitle+ "    ")
        tasks.append(Task(taskTitle,False))
        taskEntry.delete(1.0,ctk.END)
        #taskWidget.pack(side = "left")
        taskWidget.grid(row=len(tasks) - 1, column=0, sticky="W")

        taskCheckBox = ctk.CTkCheckBox(master = frame, text = "Completed?")
        #taskCheckBox.pack(side="right")
        taskCheckBox.grid(row=len(tasks) - 1, column=1, sticky="E")
    
    
window = ctk.CTk()
window.title("To Do App")
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
frame = ctk.CTkScrollableFrame(master = window, width = 800, height = 400)
frame.place(x = WINDOW_WIDTH/2 -600, y = WINDOW_HEIGHT/8)

taskEntry = ctk.CTkTextbox(master=window, width =700, height = 50)
taskEntry.place(x=WINDOW_WIDTH/2 -600, y = WINDOW_HEIGHT/8 -100)

taskAddButton = ctk.CTkButton(master = window, width = 100, height = 50, fg_color="white", text_color="black", text= "Add Task", border_color="black",border_width=2, hover_color="light gray",command = addTask)
taskAddButton.place(x= WINDOW_WIDTH/2 +125, y = WINDOW_HEIGHT/8 -100)



window.mainloop()