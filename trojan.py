from github import Github
import os
from dotenv import load_dotenv
# Function to upload a file
def upload_file(file_path, commit_message, folder_path, branch):
    with open(file_path, "r") as file:
        content = file.read()

    # Target file path  in the repository
    file_name = file_path.split("/")[-1]
    git_path = f"{folder_path}/{file_name}"

    # Check if the file exists in the target branch
    try:
        contents = repo.get_contents(git_path, ref=branch)
        # If file exists, update it
        repo.update_file(contents.path, commit_message, content, contents.sha, branch=branch)
        print(f"Updated {git_path} on branch {branch}.")
    except Exception as e:
        # If file doesn't exist, create it
        repo.create_file(git_path, commit_message, content, branch=branch)
        print(f"Created {git_path} on branch {branch}.")

load_dotenv()

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
REPO_NAME = os.getenv('REPO_NAME')
BRANCH = "data"
FOLDER_PATH = os.getenv('envtest')

g = Github(ACCESS_TOKEN)

# Get the repository
repo = g.get_repo(REPO_NAME)

# Example usage
file_to_upload = "test.txt"  # Replace with the path to your local file
commit_message = "Add data from machine_name_here"
upload_file(file_to_upload, commit_message, FOLDER_PATH, BRANCH)