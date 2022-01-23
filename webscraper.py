from bs4 import BeautifulSoup
import requests

url = ''
response = requests.get(url)
content = BeautifulSoup(response.content, "html.parser").prettify()

print (response.content)
