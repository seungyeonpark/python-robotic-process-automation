import msoffcrypto
import openpyxl as excel

fin = open("./input/test_encrypt.xlsx", "rb")
msfile = msoffcrypto.OfficeFile(fin)

msfile.load_key(password="1234")

fout = open("./output/test_decrypt.xlsx", "wb")
msfile.decrypt(fout)

book = excel.load_workbook("./output/test_decrypt.xlsx", data_only=True)
sheet = book.active
for row in sheet["A2:F99"]:
    values = [v.value for v in row]

    if values[0] is None:
        break

    print(values)

