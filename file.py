import sys
import window
import tkinter as tk
from tkinter import ttk

def open_file():
    return


def save_file():
    return


def clear():
    window.enter_demand_1.delete('0',tk.END)
    window.enter_demand_el.delete('0', tk.END)
    window.enter_supply_1.delete('0', tk.END)
    window.enter_supply_el.delete('0', tk.END)
    window.enter_fix_tax.delete('0', tk.END)
    window.enter_prop_tax.delete('0', tk.END)
    pass

def quit_app():
    sys.exit(0)