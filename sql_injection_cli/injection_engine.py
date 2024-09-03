# sql_injection_cli/injection_engine.py

import requests
from urllib.parse import urljoin

class InjectionEngine:
    def __init__(self, target_url):
        self.target_url = target_url

    def inject(self, form_details, payload):
        """Injects SQL payloads into the identified input fields."""
        target_url = urljoin(self.target_url, form_details['action'])
        data = {name: payload for input in form_details['inputs'] for name in input}
        if form_details['method'].lower() == 'post':
            response = requests.post(target_url, data=data)
        else:
            response = requests.get(target_url, params=data)
        return response.text
