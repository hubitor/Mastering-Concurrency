import requests
from bs4 import BeautifulSoup

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

root_url = 'http://www.thesaurus.com/browse/'

while True:
    print('Ctrl + C to quit.')

    my_input = input('Enter a word for scraped synonyms: ').strip()
    html_source = get_html_source(root_url + my_input)

    if html_source:
        synonyms = get_synonyms_from_html(html_source)
        if len(synonyms):
            print('%i synonyms found for %s:' % (len(synonyms), my_input))
            print(synonyms)
        else:
            print('No synonym found for %s.' % my_input)
