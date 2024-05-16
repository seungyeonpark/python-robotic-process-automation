import tkinter as tk
import tkinter.messagebox as mb
import tkinter.filedialog as fd

tk.Tk().withdraw()

filepath = fd.askopenfilename()

mb.showinfo('선택 파일', filepath)
