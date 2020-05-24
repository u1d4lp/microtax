import tkinter as tk
from tkinter import ttk
import os

def show():
    about_win = tk.Tk()
    about_win.title("About microtax")
    about_win.resizable(False, False)
    ttk.Label(about_win, text="\tVersion\n").grid(column=0, row=0)
    ttk.Label(about_win, text="\tLicence\n").grid(column=0, row=1)
    ttk.Label(about_win, text="\tBy\n").grid(column=0, row=2)
    ttk.Label(about_win, text="\tGithub\n").grid(column=0, row=3)
    ttk.Label(about_win, text="\tLinkedIn\n").grid(column=0, row=4)
    ttk.Label(about_win, text="\t1.0\t\n").grid(column=1, row=0)
    ttk.Label(about_win, text="\tMIT Licence\t\n").grid(column=1, row=1)
    ttk.Label(about_win, text="\tPaulo Vidal\t\n").grid(column=1, row=2)
    ttk.Label(about_win, text="\thttps://github.com/u1d4lp\t\n").grid(column=1, row=3)
    ttk.Label(about_win, text="\thttps://www.linkedin.com/in/paulo-vidal-30b160163/\t\n").grid(column=1, row=4)
    about_win.mainloop()


def manual():
    os.startfile("manual.html")
