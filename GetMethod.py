# import requests module
import requests

url = "https://www.formula1.com/en.html"

try:
    r = requests.get(url, timeout=1)
    r.raise_for_status()
except requests.exceptions.HTTPError as errh:
    print("HTTP Error")
    print(errh.args[0])

print(r)