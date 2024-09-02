import requests
import json

class GitHubScraper:
    def __init__(self, repo_url, token):
        self.repo_url = repo_url
        self.token = token

    def get_latest_version_info(self):
        # Extract the repository name from the URL
        repo_name = self.repo_url.split("/")[-1]
        api_url = f"https://api.github.com/repos/langchain-ai/{repo_name}/releases/latest"

        headers = {
            "Authorization": f"token {self.token}"
        }

        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            latest_release = response.json()
            return {
                "version": latest_release["tag_name"],
                "summary": latest_release["body"]
            }
        else:
            return {
                "version": "N/A",
                "summary": "Could not fetch release information."
            }
