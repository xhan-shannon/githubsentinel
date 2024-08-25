import smtplib

class NotificationManager:
    def send_notification(self, repo, updates):
        # Send email notifications to the team
        subject = f"New Updates for '{repo}' Repository"
        body = f"The following updates have been made to the '{repo}' repository:\n\n"
        for commit in updates:
            body += f"- {commit['commit']['message']} by {commit['commit']['author']['name']}\n"

        sender = "github-sentinel@your-company.com"
        recipients = ["team@your-company.com"]

        message = f"Subject: {subject}\n\n{body}"
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login("your-email@gmail.com", "your-password")
            smtp.sendmail(sender, recipients, message)
