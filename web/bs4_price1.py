from bs4 import BeautifulSoup

hfile = './input/book_static.html'

with open(hfile, encoding='utf-8') as fp:
    html_str = fp.read()

soup = BeautifulSoup(html_str, 'html5lib')

item = soup.find(id='b1', class_='item')

for e in item.descendants:
    if e.name == 'div':
        if 'price' in e['class']:
            print(e.string)
