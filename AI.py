from google import genai

api_key =  input("Please enter the API key: ")

client = genai.Client(api_key = api_key)
chat = client.chats.create(model="gemini-3.5-flash-lite")

response = chat.send_message("""
You are operating a to do app.
Where you may have to summarize the user's tasks.
You may have to order them in terms of difficulty and return the reordered items.
""")

#print(response.text)

class Task:
    def __init__(self, description, completed = False) -> None:
        self.title = get_title(description)
        self.description = description
        self.completed = completed

def get_title(description: str):
    prompt = f"""Here is a description of a task that the user wants to do:

\"{description}\"

Can you generate a title to be shown above the description of the task, please try to keep it below 30 characters and don't use * characters."""

    response = chat.send_message(prompt)
#    print(response.text)

    return response.text.strip()
    

def reorder_tasks(tasks: list[Task], ascending = True):
    if ascending:
        ascending_str = "ascending"

    else:
        ascending_str = "descending"

    prompt = f"Here are a bunch of tasks that you need to reorder in {ascending_str} order:\n\n"

    for i in range(len(tasks)):
        prompt += f"Task number {i}: {tasks[i].title}\n"

    prompt += """
Please can you respond with your answer with the task numbers separated by \\n only, such as the example of 0, 3, 1, 2 would look like:
0
3
1
2

Can you please refrain from responding with any other text, if you can't decide the order of two different tasks, just use your best guess.
Please also do not skip or repeat any task numbers."""

    response = chat.send_message(prompt).text.strip()

    ordered_tasks = []

    for str_i in response.split("\n"):
        i = int(str_i)
        ordered_tasks.append(tasks[i])

    return ordered_tasks

# response = chat.send_message("Generate a random number.")
# print(response.text)

# response = chat.send_message("Now what is the full name of the account holder?")
# print(response.text)


tasks = [
    Task("Brush my teeth"),
    Task("Learn python from scratch"),
    Task("Learn binary multiplication"),
    Task("Start revising for my Year 12 end of year exam"),
    Task("feed my cat"),
]


for i in range(len(tasks)):
    print(f"Task number {i}:\nDescription: {tasks[i].description}\nTitle: {tasks[i].title}\n")

print()

ordered_tasks = reorder_tasks(tasks)

for i in range(len(ordered_tasks)):
    print(f"Task number {i}:\nDescription: {ordered_tasks[i].description}\nTitle: {ordered_tasks[i].title}\n")