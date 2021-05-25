import requests

url = "https://www.google.com"

res = requests.get(url)
print(res.text)
