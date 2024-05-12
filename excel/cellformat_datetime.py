import openpyxl as excel
import datetime

book = excel.Workbook()
sheet = book.active

dt = datetime.datetime(
    year=2023, month=4, day=5,
    hour=11, minute=22, second=33
)
sheet.append([dt, dt, dt, dt])

sheet["A1"].number_format = 'yyyy\/mm\/dd'
sheet["B1"].number_format = 'yyyy년 mm월 dd일'
sheet["C1"].number_format = 'hh:mm:ss'
sheet["D1"].number_format = 'mm\/dd hh:mm:ss'

book.save("./output/cellformat_datetime.xlsx")

