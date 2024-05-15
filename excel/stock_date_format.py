import openpyxl as excel
import datetime

in_file = './input/stock-data.xlsx'
out_file = './output/stock_date_format.xlsx'
cell_format = 'yy\/mm/\dd'


def check_cell(cell):
    if type(cell.value) is datetime.datetime:
        cell.number_format = cell_format


def shorten_date(in_file_path, out_file_path):
    book = excel.load_workbook(in_file_path)

    for sheet in book.worksheets:
        for row in sheet.iter_rows():
            for cell in row:
                check_cell(cell)

    book.save(out_file_path)


if __name__ == '__main__':
    shorten_date(in_file, out_file)
