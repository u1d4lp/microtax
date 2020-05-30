import tkinter as tk
from tkinter import ttk
import plotting
import about
import file
import theme

main_win = tk.Tk()
main_win.title("microtax")
main_win.resizable(False, False)

# Menu
menu_bar = tk.Menu(main_win)
main_win.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar)
help_menu = tk.Menu(menu_bar)


file_menu.add_command(label="Clear", command=file.clear)
file_menu.add_command(label="Save", command=file.save)
file_menu.add_command(label="Quit", command=file.quit_app)


help_menu.add_command(label="Manual", command=about.manual)
help_menu.add_command(label="About Microtax", command=about.show)


menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Labels, column = 0

ttk.Label(main_win, text="Product maximum demand").grid(column=0, row=0)
ttk.Label(main_win, text="Demand curve elasticity").grid(column=0, row=1)
ttk.Label(main_win, text="Product minimum supply").grid(column=0, row=2)
ttk.Label(main_win, text="Supply curve elasticity").grid(column=0, row=3)
ttk.Label(main_win, text="Fixed tax per product").grid(column=0, row=4)
ttk.Label(main_win, text="Proportional tax per $1").grid(column=0, row=5)


# Textbox widgets, column = 1
demand_max = tk.IntVar()
enter_demand_max = ttk.Entry(main_win, width=12, textvariable=demand_max)
enter_demand_max.grid(column=1, row=0)

demand_el = tk.DoubleVar()
enter_demand_el = ttk.Entry(main_win, width=12, textvariable=demand_el)
enter_demand_el.grid(column=1, row=1)

supply_min = tk.IntVar()
enter_supply_min = ttk.Entry(main_win, width=12, textvariable=supply_min)
enter_supply_min.grid(column=1, row=2)

supply_el = tk.DoubleVar()
enter_supply_el = ttk.Entry(main_win, width=12, textvariable=supply_el)
enter_supply_el.grid(column=1, row=3)

fix_tax = tk.DoubleVar()
enter_fix_tax = ttk.Entry(main_win, width=12, textvariable=fix_tax)
enter_fix_tax.grid(column=1, row=4)

prop_tax = tk.DoubleVar()
enter_prop_tax = ttk.Entry(main_win, width=12, textvariable=prop_tax)
enter_prop_tax.grid(column=1, row=5)

# Apply button
apply_action = ttk.Button(main_win, text="Plot", command=plotting.show_plt)
apply_action.grid(column=0, row=6)

# Random button
random_action = ttk.Button(main_win, text="Randomize", command=plotting.random_plt)
random_action.grid(column=1, row=6)
