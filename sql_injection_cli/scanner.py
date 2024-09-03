# sql_injection_cli/scanner.py

import requests
from bs4 import BeautifulSoup

class Scanner:
    def __init__(self, url):
        self.url = url

    def scan(self):
        """Crawls the target website to find input fields and parameters."""
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        forms = soup.find_all('form')
        inputs = []
        for form in forms:
            form_action = form.get('action') or self.url
            form_method = form.get('method') or 'get'
            form_inputs = form.find_all('input')
            inputs.append({
                'action': form_action,
                'method': form_method,
                'inputs': [{input.get('name'): input.get('value', '')} for input in form_inputs]
            })
        return inputs
