import requests

response = requests.get("https://api.github.com/")
print(response.url)
print(response.headers)
print(response.elapsed)
print(response.json())
print(response.ok)
print(response.links)


# response.status_code returns the status code from the headers 
# itself, to check if successful