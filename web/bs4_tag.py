from bs4 import BeautifulSoup

hfile = './input/book_static.html'

with open(hfile, encoding='utf-8') as fp:
    html_str = fp.read()

soup = BeautifulSoup(html_str, 'html5lib')

print(soup.title)
print(soup.find('title'))
print(soup.select_one('title'))

print(soup.find_all('title'))
print(soup.select('title'))
