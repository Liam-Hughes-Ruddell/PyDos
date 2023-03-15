import urllib.request

url = "https://www.example.com" // replace with your website
response = urllib.request.urlopen(url)

print(response.read())
