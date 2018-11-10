import requests
from bs4 import BeautifulSoup

import threading

from timeit import default_timer as timer


ROOT_URL = 'http://www.thesaurus.com/browse/'

def get_html_source(url):
    try:
        r = requests.get(url)
        return r.text

    except Exception as e:
        print('There was a problem: %s.' % e)
        return False

def get_synonyms_from_html(html_source):
    soup = BeautifulSoup(html_source, 'html.parser')
    html_synonyms = soup.select('section.MainContentContainer > section > section > ul > li > span > a')

    return [item.getText() for item in html_synonyms]


my_input = input('Enter a list of words for scraped synonyms (separated by commas): ')
print()

start = timer()
words = my_input.split(',')

for word in words:
    html_source = get_html_source(ROOT_URL + word.strip())

    if html_source:
        synonyms = get_synonyms_from_html(html_source)
        print('%i synonyms found for %s: %s\n' % (len(synonyms), word, str(synonyms)))

print('Took %.2f seconds' % (timer() - start))
