from bs4 import BeautifulSoup

hfile = './input/scraping.html'
with open(hfile, encoding='utf-8') as fp:
    html_str = fp.read()

soup = BeautifulSoup(html_str, 'html5lib')

head = soup.head
print('head의 부모: ', head.parent.name)
print('head의 부모의 부모', head.parent.parent.name)

print('head의 자식')
for e in head.contents:
    print('[{0}]{1}'.format(type(e), e.name))
