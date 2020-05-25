import matplotlib.pyplot as plt
import numpy as np
import calc
import window
import randomplt

def show_plt():
    fig = plt.figure()
    ax = plt.axes()
    ax.set_title('Supply and demand of product X\n')
    ax.set_xlabel('Quantity\n')
    ax.set_ylabel('Price')
    price_when_demand_0 = int(int(window.demand_1.get())/(int(window.demand_el.get())))
    price = np.linspace(1, price_when_demand_0, 100000)
    calc.demand_curve = plt.plot(price, window.demand_1.get() - (window.demand_el.get() * (price - 1)))
    supply_curve = plt.plot(price, window.supply_1.get() + (window.supply_el.get() * (price - 1)))
    tax_supply_curve = plt.plot(price, window.supply_1.get() + window.fix_tax.get() + ((1 + window.prop_tax.get()) * (window.supply_el.get() * (price - 1))))
    calc.printc()
    plt.show()


def random_plt():
    fig = plt.figure()
    ax = plt.axes()
    ax.set_title('Supply and demand of product X\n')
    ax.set_xlabel('Quantity\n')
    ax.set_ylabel('Price')
    price_when_demand_0 = randomplt.demand_1 / randomplt.demand_el
    price = np.linspace(1, price_when_demand_0, 100000)
    calc.demand_curve = plt.plot(price, randomplt.demand_1 - (randomplt.demand_el * (price - 1)))
    supply_curve = plt.plot(price, randomplt.supply_1 + (randomplt.supply_el * (price - 1)))
    tax_supply_curve = plt.plot(price, randomplt.supply_1 + randomplt.fix_tax + ((1 + randomplt.prop_tax) * (randomplt.supply_el * (price - 1))))
    plt.show()