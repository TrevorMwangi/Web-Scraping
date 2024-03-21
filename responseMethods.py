import requests

response = requests.get("https://api.github.com/users/TrevorMwangi")
print(response.url)
print(response.content)

# response.status_code returns the status code from the headers 
# itself, to check if successful