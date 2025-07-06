import os
from eyai import Assistant


client = Assistant(
    base_url="https://api.groq.com/openai/v1",
    model="llama-3.3-70b-versatile",
    api_key="your-api-key"
)

@client.tool("Use this function to create folders")
def create_folder(folder_name: str):
    try:
        os.mkdir(folder_name)
        return "success"
    except Exception:
        return "fail"

@client.tool("Use this to read files")
def read_file(folder_name: str, file_name: str):
    try:
        path = os.path.join(".", folder_name, file_name)

        with open(path, "r") as file:
            return file.read()
    except Exception:
        return "failed to read file"

@client.tool("Use this to create files. It expects a file name, the content and the name of the folder to write into")
def write_file(file_name: str, content: str, folder_name: str):
    try:
        path = os.path.join(".", folder_name, file_name)

        with open(path, "a") as file:
            file.write(content)

        return "success"
    except Exception:
        return "failed to create file"

@client.tool("Use it to start programs using a program name eg: firefox, dolphin etc")
def start_program(progam_name: str):
    try:
        os.system(progam_name)

        return "success"
    except Exception:
        return "failed to run program"

while True:
    message = input("Your message: ")

    response = client.chat(message)

    print(response)
