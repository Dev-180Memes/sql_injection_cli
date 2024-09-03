class DetectionModule:
    def detect(self, response_text):
        """Analyzes the response for signs of SQL injection vulnerabilities."""
        error_messages = [
            "you have an error in your sql syntax;",
            "warning: mysql",
            "unclosed quotation mark",
            "quoted string not properly terminated"
        ]
        for error_message in error_messages:
            if error_message.lower() in response_text.lower():
                return True
        return False
