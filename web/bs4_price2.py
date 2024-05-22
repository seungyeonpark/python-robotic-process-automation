from bs4 import BeautifulSoup

hfile = './input/book_static.html'

with open(hfile, encoding='utf-8') as fp:
    html_str = fp.read()

soup = BeautifulSoup(html_str, 'html5lib')

item = soup.find('div', id='b1')
p = item.find(class_='price')
print(p.string)

p = soup.select_one('#b1 .price')
print(p.string)
