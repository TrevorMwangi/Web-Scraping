import requests
from requests.auth import HTTPBasicAuth

response = requests.get("https://api.github.com/",
                        auth = HTTPBasicAuth("TrevorMwangi", "EternalAtakeno.1!"))

print(response)