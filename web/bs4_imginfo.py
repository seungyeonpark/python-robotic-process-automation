from bs4 import BeautifulSoup
import csv
import os

hfile = './server/templates/book_static.html'

with open(hfile, encoding='utf-8') as fp:
    html_str = fp.read()

soup = BeautifulSoup(html_str, 'html5lib')

img_list = soup.select('#gallery-section img')
imginfo = []

for img in img_list:
    relpath = img['src']
    basedir = os.path.dirname(hfile)
    join_path = os.path.join(basedir, relpath)
    abs_path = os.path.abspath(join_path)

    size = str(os.path.getsize(abs_path))

    img_tp = (os.path.basename(abs_path), size + "byte")
    print(img_tp)

    imginfo.append(img_tp)

with open('./output/imginfo.csv', 'wt', encoding='utf-8', newline='') as fp:
    csv.writer(fp).writerows(imginfo)

