from bs4 import BeautifulSoup

hfile = './input/scraping.html'
with open(hfile, encoding='utf-8') as fp:
    html_str = fp.read()

soup = BeautifulSoup(html_str, 'html5lib')
print(soup.prettify() + '\n')

title = soup.title
print(title)
print(title.string + '\n')

print(type(soup))
print(type(title))
print(type(title.string))
