# import requests module 
import requests 

# create a session object 
s = requests.Session() 

# make a get request 
s.get('https://httpbin.org/cookies/set/sessioncookie/123456789') 

# again make a get request 
r = s.get('https://httpbin.org/cookies') 

# check if cookie is still set 
print(r.text) 

''' illustrating the use of session objects by setting a cookie to a URL 
    and then making a request again to check if the cookie is set '''
