import tkinter as tk
from tkinter import ttk
from tkinter import *

style = 'seaborn'


def show():
    theme_win = tk.Tk()
    theme_win.title("Theme config")
    theme_win.resizable(False, False)
    Radiobutton(theme_win, text="Default colors", variable=style, value='default').pack(anchor=W)
    Radiobutton(theme_win, text="Seaborn Colors", variable=style, value='seaborn').pack(anchor=W)
    theme_win.mainloop()


