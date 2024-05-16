import tkinter as tk
import tkinter.messagebox as mb
import tkinter.filedialog as fd

tk.Tk().withdraw()

dir_path = fd.askdirectory(
    title='폴더를 지정해주세요',
    initialdir='./'
)

mb.showinfo('선택 폴더', dir_path)
