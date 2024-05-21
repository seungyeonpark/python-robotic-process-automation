from bs4 import BeautifulSoup

hfile = './input/book_static.html'

with open(hfile, encoding='utf-8') as fp:
    html_str = fp.read()
soup = BeautifulSoup(html_str, 'html5lib')

print(soup.find(id='b1', class_='item'))
print(soup.find(name='div', attrs={'id': 'b1', 'class': 'item'}))
print(soup.find_all('div', class_='item', limit=1))
print(soup.select_one('div#b1.item'))
print('--------------')

print(soup.find(string='도커, 컨테이너 빌드업!'))
print(soup.find('div', string='도커, 컨테이너 빌드업!'))
print('--------------')

element = soup.find(string='파이썬 머신러닝')
print(element)
print(element.parent)
print(element.parent.parent)
