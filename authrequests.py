import requests
from requests.auth import HTTPBasicAuth

response = requests.get("https://api.github.com/",
                        auth = HTTPBasicAuth("Trevor", "password"))

print(response)