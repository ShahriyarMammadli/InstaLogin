# Shahriyar Mammadli
# This is a template for logging in to Instagram
# Import required libraries
from bs4 import BeautifulSoup
import json, re, requests
import time

# Provide username and password
username = ''
password = ''

url = 'https://www.instagram.com/accounts/login/'

# csrf token is needed to be able to login, thus first we create a session to get it
session = requests.Session()
# Setting up headers
session.headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
session.headers.update({'Referer': url})
# Send the request to obtain csrf
csrfRequest = session.get(url)
# Get the script object to retrieve the json from it
script = BeautifulSoup(csrfRequest.content, 'html.parser').find('body').find("script", text=re.compile('window._sharedData'))
# Convert string to the json
data = json.loads(script.string.split("window._sharedData = ")[1][:-1])
# Get the csrf from the json
csrf = data['config'].get('csrf_token')

# enc_password must be used for logging in
epochTime = str(int(time.time()))
encPass = '#PWD_INSTAGRAM_BROWSER:0:' + epochTime + ':' + password
login_data = {'username': username, 'enc_password': encPass}
session.headers.update({'X-CSRFToken': csrf})
login = session.post(url + "ajax/", data=login_data, allow_redirects=True)
print(login.content)