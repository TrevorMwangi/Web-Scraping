import requests

response = requests.get("https://api.github.com/")
print(response.url)
print(response.headers)
print(response.elapsed)


# response.status_code returns the status code from the headers 
# itself, to check if successful