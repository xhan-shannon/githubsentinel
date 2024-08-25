import requests

class GitHubScraper:
    def get_scrubbed_repos(self):
        # Fetch the list of scrubbed GitHub repositories
        response = requests.get("https://api.github.com/users/your-organization/repos")
        repos = [repo['name'] for repo in response.json() if repo['private']]
        return repos

    def get_repo_updates(self, repo):
        # Fetch the latest updates for the given repository
        response = requests.get(f"https://api.github.com/repos/your-organization/{repo}/commits")
        commits = response.json()
        return commits
