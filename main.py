import customtkinter as ctk
import openai
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900
class Task():
    def __init__(self, title: str, description:str, completed:bool):
        self.title = title
        self.description = description
        self.completed = completed
tasks:list[Task] = []


window = ctk.CTk()
window.title("To Do App")
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

window.mainloop()