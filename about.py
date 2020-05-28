import tkinter as tk
from tkinter import ttk
import webbrowser
import os

def show():
    about_win = tk.Tk()
    about_win.title("About microtax")
    about_win.resizable(False, False)
    ttk.Label(about_win, text="\tVersion\n").grid(column=0, row=0)
    ttk.Label(about_win, text="\tLicence\n").grid(column=0, row=1)
    ttk.Label(about_win, text="\tBy\n").grid(column=0, row=2)
    githublink = ttk.Button(about_win, text="Github", command=webbrowser.open_new(r"https://github.com/u1d4lp.html"))
    githublink.grid(column=0, row=3)
    linkedinlink = ttk.Button(about_win, text="LinkedIn", command=webbrowser.open_new(r"https://www.linkedin.com/in/paulo-vidal-30b160163/"))
    linkedinlink.grid(column=0, row=4)
    ttk.Label(about_win, text="\t1.0\t\n").grid(column=1, row=0)
    ttk.Label(about_win, text="\tMIT Licence\t\n").grid(column=1, row=1)
    ttk.Label(about_win, text="\tPaulo Vidal\t\n").grid(column=1, row=2)
    about_win.mainloop()


def manual():
    os.startfile("manual.html")
