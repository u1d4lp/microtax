import sys
import window
import tkinter as tk
from tkinter import ttk

def open_file():
    return


def save():
    f = open("plot.txt", "w+")
    return


def clear():
    window.enter_demand_max.delete('0',tk.END)
    window.enter_demand_el.delete('0', tk.END)
    window.enter_supply_min.delete('0', tk.END)
    window.enter_supply_el.delete('0', tk.END)
    window.enter_fix_tax.delete('0', tk.END)
    window.enter_prop_tax.delete('0', tk.END)
    pass

def quit_app():
    sys.exit(0)
