import matplotlib.pyplot as plt
import numpy as np
import calc
import window

def show_plt():
    fig = plt.figure()
    ax = plt.axes()
    price_when_demand_0 = int(int(window.demand_1.get())/(int(window.demand_el.get())))
    price = np.linspace(1, price_when_demand_0, 100000)
    calc.demand_curve = plt.plot(price, window.demand_1.get() - (window.demand_el.get() * (price - 1)))
    supply_curve = plt.plot(price, window.supply_1.get() + (window.supply_el.get() * (price - 1)))
    tax_supply_curve = plt.plot(price, window.supply_1.get() + window.fix_tax.get() + ((1 + window.prop_tax.get()) * (window.supply_el.get() * (price - 1))))
    plt.show()
    calc.printc()

def random_plt():
    pass