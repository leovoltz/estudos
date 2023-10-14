# Requests para requisições HTTP
import requests

# http:// -> 80
# https:// -> 443
url = 'http://127.0.0.1:3333/'
response = requests.get(url)

print(response.status_code)
# print(response.headers)
# print(response.content)
print(response.text)
