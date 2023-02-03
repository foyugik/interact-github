import requests

# Set the GitHub API endpoint URL
endpoint_url = "https://api.github.com/repos/<username>/<repository>"

# Set the API endpoint URL to retrieve information about a specific repository
repo_url = endpoint_url.replace("<username>", "<username>").replace("<repository>", "<repository>")

# Send a GET request to the API endpoint to retrieve information about the repository
response = requests.get(repo_url)

# Print the response from the API
print(response.json())
