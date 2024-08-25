import os

class ReportGenerator:
    def generate_report(self, repo, updates):
        # Generate a report for the given repository and updates
        report_dir = "reports"
        if not os.path.exists(report_dir):
            os.makedirs(report_dir)

        report_path = os.path.join(report_dir, f"{repo}_report.md")
        with open(report_path, "w") as report_file:
            report_file.write(f"# Updates for '{repo}' Repository\n\n")
            for commit in updates:
                report_file.write(f"- {commit['commit']['message']} by {commit['commit']['author']['name']}\n")
        print(f"Report generated: {report_path}")
