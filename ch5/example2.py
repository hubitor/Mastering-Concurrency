import requests

url = 'http://www.thesaurus.com/browse/pythonic'

r = requests.get(url)

print(r.status_code)
print(r.headers)

with open('pythonic_thesaurus.html', 'w') as f:
    f.write(r.text)

print('Done.')
