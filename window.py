import tkinter as tk
from tkinter import ttk
import plotting
import about
import file

main_win = tk.Tk()
main_win.title("microtax")
main_win.resizable(False, False)

# Menu
menu_bar = tk.Menu(main_win)
main_win.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar)
edit_menu = tk.Menu(menu_bar)
appearance_menu = tk.Menu(menu_bar)
help_menu = tk.Menu(menu_bar)


file_menu.add_command(label="Clear", command=file.clear)
file_menu.add_command(label="Quit", command=file.quit_app)

edit_menu.add_command(label="Theme")
edit_menu.add_command(label="Resizable")
edit_menu.add_command(label="Font")

help_menu.add_command(label="Manual", command=about.manual)
help_menu.add_command(label="About Microtax", command=about.show)


menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Labels, column = 0

ttk.Label(main_win, text="\tProduct demand when price is $1\n").grid(column=0, row=1)
ttk.Label(main_win, text="\tDemand curve elasticity\n").grid(column=0, row=2)
ttk.Label(main_win, text="\n\tEnter supply definitions\n").grid(column=0, row=3)
ttk.Label(main_win, text="\tProduct supply when price is $1\n").grid(column=0, row=4)
ttk.Label(main_win, text="\tSupply curve elasticity\n").grid(column=0, row=5)
ttk.Label(main_win, text="\n\tEnter tax options\n").grid(column=0, row=6)
ttk.Label(main_win, text="\tFixed tax per product\n").grid(column=0, row=7)
ttk.Label(main_win, text="\tProportional tax per $1\n").grid(column=0, row=8)

# Empty column
ttk.Label(main_win, text="     ").grid(column=1, row=0)


# Textbox widgets, column = 1
demand_1 = tk.IntVar()
enter_demand_1 = ttk.Entry(main_win, width=12, textvariable=demand_1)
enter_demand_1.grid(column=1, row=1)

demand_el = tk.DoubleVar()
enter_demand_el = ttk.Entry(main_win, width=12, textvariable=demand_el)
enter_demand_el.grid(column=1, row=2)

supply_1 = tk.IntVar()
enter_supply_1 = ttk.Entry(main_win, width=12, textvariable=supply_1)
enter_supply_1.grid(column=1, row=4)

supply_el = tk.DoubleVar()
enter_supply_el = ttk.Entry(main_win, width=12, textvariable=supply_el)
enter_supply_el.grid(column=1, row=5)

fix_tax = tk.DoubleVar()
enter_fix_tax = ttk.Entry(main_win, width=12, textvariable=fix_tax)
enter_fix_tax.grid(column=1, row=7)

prop_tax = tk.DoubleVar()
enter_prop_tax = ttk.Entry(main_win, width=12, textvariable=prop_tax)
enter_prop_tax.grid(column=1, row=8)

# Apply button
apply_action = ttk.Button(main_win, text="Plot", command=plotting.show_plt)
apply_action.grid(column=0, row=9)



# Random button
random_action = ttk.Button(main_win, text="Randomize", command=plotting.random_plt)
random_action.grid(column=1, row=9)
