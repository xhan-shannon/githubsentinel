from scraper import GitHubScraper
from notification import NotificationManager
from report import ReportGenerator


def main():
    config = load_config()

    # Initialize the components
    scraper = GitHubScraper(config["github_repo"], config["github_token"])
    notifier = NotificationManager(config)
    reporter = ReportGenerator()

    # Load subscriptions
    with open('subscription.json') as sub_file:
        subscriptions = json.load(sub_file)["subscriptions"]

    for subscription in subscriptions:
        if subscription["enabled"]:
            # Fetch the latest version information for subscribed repos
            latest_version_info = scraper.get_latest_version_info()

            if subscription["notify_on_release"]:
                # Notify the team about the latest version
                notifier.send_notification(config["email_recipients"], latest_version_info)

            # Generate a report
            reporter.generate_report(latest_version_info)


if __name__ == "__main__":
    main()

