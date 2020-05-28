import tkinter as tk
from tkinter import ttk
import webbrowser
import os

def show():
    about_win = tk.Tk()
    about_win.title("About microtax")
    about_win.resizable(False, False)
    ttk.Label(about_win, text="Version").grid(column=0, row=0)
    ttk.Label(about_win, text="Licence").grid(column=0, row=1)
    ttk.Label(about_win, text="By").grid(column=0, row=2)
    githublink = ttk.Button(about_win, text="Github", command=open_github_link)
    githublink.grid(column=0, row=3)
    linkedinlink = ttk.Button(about_win, text="LinkedIn", command=open_linkedin_link)
    linkedinlink.grid(column=1, row=3)
    ttk.Label(about_win, text="0.9").grid(column=1, row=0)
    ttk.Label(about_win, text="MIT Licence").grid(column=1, row=1)
    ttk.Label(about_win, text="Paulo Vidal").grid(column=1, row=2)
    about_win.mainloop()


def manual():
    os.startfile("manual.html")


def open_github_link():
    webbrowser.open_new(r"https://github.com/u1d4lp.html")

def open_linkedin_link():
    webbrowser.open_new(r"https://www.linkedin.com/in/paulo-vidal-30b160163/")