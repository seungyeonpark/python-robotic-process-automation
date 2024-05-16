import tkinter as tk
import tkinter.messagebox as mb
import tkinter.simpledialog as sd

tk.Tk().withdraw()

name = sd.askstring(
    '성명 입력', '성명을 입력해주세요.\n(미입력 시 종료)', initialvalue='sypark'
)

if name == '' or name is not None:
    quit()

mb.showinfo('인사', f'{name}님 안녕하세요')
