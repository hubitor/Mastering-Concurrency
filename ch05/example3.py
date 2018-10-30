from bs4 import BeautifulSoup

with open('pythonic_thesaurus.html') as f:
    html_source = f.read()

soup = BeautifulSoup(html_source, 'html.parser')

html_synonyms = soup.select('div.MainContentContainer > div > section > ul > li > span > a')

text_synonyms = [item.getText() for item in html_synonyms]
print(text_synonyms)
