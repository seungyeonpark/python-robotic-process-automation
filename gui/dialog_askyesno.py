import tkinter as tk
import tkinter.messagebox as mb

tk.Tk().withdraw()

yes_no = mb.askyesno('질문', '처리를 실행하시겠습니까?')

if yes_no:
    mb.showinfo('알림', '실행 완료')
else:
    mb.showinfo('알림', '실행하지 않음')
