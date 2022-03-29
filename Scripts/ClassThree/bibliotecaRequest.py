import requests as r

info = r.get("https://github.com/")
info.headers

print(info.headers['date'])
print(info.headers['server'])
print(info.encoding)