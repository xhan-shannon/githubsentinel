from scraper import GitHubScraper
from notification import NotificationManager
from report import ReportGenerator

def main():
    # Initialize the components
    scraper = GitHubScraper()
    notifier = NotificationManager()
    reporter = ReportGenerator()

    # Fetch the scrubbed GitHub repos
    repos = scraper.get_scrubbed_repos()

    # Collect the updates for each repo
    for repo in repos:
        updates = scraper.get_repo_updates(repo)

        # Notify the team about the updates
        notifier.send_notification(repo, updates)

        # Generate a report
        reporter.generate_report(repo, updates)

if __name__ == "__main__":
    main()
