import requests

r = requests.get("https://api.github.com/users/TrevorMwangi")
print(r)

print(r.content)