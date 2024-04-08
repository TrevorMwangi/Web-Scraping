import requests
from bs4 import BeautifulSoup

# Making a GET request
r = requests.get("https://www.bbc.com/news")

# check status code for response
print(r)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())