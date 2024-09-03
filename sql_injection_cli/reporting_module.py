class ReportingModule:
    def generate_report(self, vulnerabilities):
        """Generates a report of the identified vulnerabilities."""
        report = "SQL Injection Vulnerability Report\n"
        report += "="*40 + "\n\n"
        for vulnerability in vulnerabilities:
            report += f"Vulnerability Found at {vulnerability['url']}\n"
            report += f"Payload: {vulnerability['payload']}\n\n"
        with open("report.txt", "w") as file:
            file.write(report)
