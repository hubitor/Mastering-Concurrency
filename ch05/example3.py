from bs4 import BeautifulSoup

with open('pythonic_thesaurus.html') as f:
    html_source = f.read()

soup = BeautifulSoup(html_source, 'html.parser')

html_synonyms = soup.select('section.MainContentContainer > section > section > ul > li > span > a')

text_synonyms = [item.getText() for item in html_synonyms]
print(text_synonyms)
