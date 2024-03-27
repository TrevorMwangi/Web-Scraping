import requests

response = requests.get("https://api.github.com/")
print(response.url)
print(response.headers)
print(response.elapsed)
print(response.json())
print(response.ok)
print(response.links)
print(response.history)


'''	response.headers returns a dictionary of response headers.
 	response.encoding returns the encoding used to decode response.content.
 	response.elapsed returns a timedelta object with the time elapsed from sending the request to the arrival of the response.
 	response.close() closes the connection to the server.
 	response.content returns the content of the response, in bytes.
 	response.cookies returns a CookieJar object with the cookies sent back from the server.
 	response.history returns a list of response objects holding the history of request (url).
 	response.is_permanent_redirect returns True if the response is the permanent redirected url, otherwise False.
 	response.is_redirect returns True if the response was redirected, otherwise False.
 	response.iter_content() iterates over the response.content.
 	response.json() returns a JSON object of the result (if the result was written in JSON format, if not it raises an error).
 	response.url returns the URL of the response.
 	response.text returns the content of the response, in unicode.
 	response.status_code returns a number that indicates the status (200 is OK, 404 is Not Found).
	response.request returns the request object that requested this response.
 	response.reason returns a text corresponding to the status code.
 	response.raise_for_status() returns an HTTPError object if an error has occurred during the process.
 	response.ok returns True if status_code is less than 200, otherwise False.
 	response.links returns the header links. '''