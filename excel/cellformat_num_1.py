import openpyxl as excel

book = excel.Workbook()
sheet = book.active

val = 3.141592
sheet.append([val, val, val])

sheet["A1"].number_format = '0'
sheet["B1"].number_format = '0.00'
sheet["C1"].number_format = '0.0000'

book.save("./output/cellformat_num_1.xlsx")

