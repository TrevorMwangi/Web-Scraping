import requests
from bs4 import BeautifulSoup

# Making a GET request
r = requests.get("https://www.geeksforgeeks.org/python-programming-language/")

# check status code for response
print(r)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())