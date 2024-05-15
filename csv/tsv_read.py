import csv

with open('./input/items3.tsv', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='\t')

    for row in reader:
        print(row)