import openpyxl as excel

book = excel.Workbook()

sheet = book.active

sheet["A1"] = "Hello Excel"

book.save("./output/hello.xlsx")
