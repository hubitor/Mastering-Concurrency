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
    html_synonyms = soup.select('div.MainContentContainer > div > section > ul > li > span > a')

    return [item.getText() for item in html_synonyms]

class MyThread(threading.Thread):
    def __init__(self, word):
        threading.Thread.__init__(self)
        self.word = word

    def run(self):
        html_source = get_html_source(ROOT_URL + word)

        if html_source:
            synonyms = get_synonyms_from_html(html_source)
            print('%i synonyms found for %s: %s\n' % (len(synonyms), word, str(synonyms)))


my_input = input('Enter a list of words for scraped synonyms (separated by commas): ')

start = timer()
words = my_input.split(',')

threads = []
for word in words:
    temp_thread = MyThread(word.strip())
    temp_thread.start()

    threads.append(temp_thread)

for thread in threads:
    thread.join()

print('Took %.2f seconds' % (timer() - start))
