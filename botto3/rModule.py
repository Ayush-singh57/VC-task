import requests

r = requests.get('https://www.google.com')
print(r.text)

with open('index.html', 'w') as f:
    f.write(r.text)