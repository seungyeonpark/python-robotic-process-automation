import tkinter as tk
import tkinter.messagebox as mb
import tkinter.filedialog as fd
import tkinter.simpledialog as sd

tk.Tk().withdraw()


def info(message, title='정보'):
    mb.showinfo(title, message)


def warning(message, title='경고'):
    mb.showwarning(title, message)


def yesno(message, title='질문'):
    return mb.askyesno(title, message)


def input(message, title='입력', value=''):
    return sd.askstring(title, message, initialvalue=value)


def select_file(init_dir='./'):
    return fd.askopenfilename(initialdir=init_dir)


def select_save_file(init_dir='./'):
    return fd.asksaveasfilename(initialdir=init_dir)


def select_dir(init_dir='./'):
    return fd.askdirectory(initialdir=init_dir)
