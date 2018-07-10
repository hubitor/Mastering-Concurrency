import requests

url = 'http://www.thesaurus.com/browse/pythonic'

r = requests.get(url)

with open('pythonic_thesaurus.html', 'w') as f:
    f.write(r.text)

print('Done.')
