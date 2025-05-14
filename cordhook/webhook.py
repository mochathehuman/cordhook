import requests
from .exceptions import WebhookException

class Webhook:
    def __init__(self, url):
        self.url = url
        self.payload = {"content": "", "embeds": []}
        self.files = None

    def set_content(self, content):
        self.payload["content"] = content
        return self

    def add_embed(self, title, description, color=0x5865F2):
        embed = {
            "title": title,
            "description": description,
            "color": color
        }
        self.payload["embeds"].append(embed)
        return self

    def attach_file(self, file_path):
        self.files = {"file": open(file_path, "rb")}
        return self

    def send(self):
        headers = {"Content-Type": "application/json"}
        try:
            if self.files:
                response = requests.post(
                    self.url, 
                    data={"payload_json": str(self.payload)}, 
                    files=self.files
                )
            else:
                response = requests.post(
                    self.url, 
                    json=self.payload, 
                    headers=headers
                )
            if response.status_code != 204:
                raise WebhookException(f"Failed to send webhook: {response.status_code} - {response.text}")
        finally:
            if self.files:
                self.files["file"].close()
