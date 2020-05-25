import matplotlib.pyplot as plt
import numpy as np
import calc
import window
import random

random_counter = 0

def show_plt():
    fig = plt.figure()
    ax = plt.axes()
    ax.set_title('Supply and demand of product X\n')
    ax.set_xlabel('Quantity\n')
    ax.set_ylabel('Price')
    price_when_demand_0 = int(int(window.demand_1.get()) / (int(window.demand_el.get())))
    price = np.linspace(1, price_when_demand_0, 100000)
    calc.demand_curve = plt.plot(price, window.demand_1.get() - (window.demand_el.get() * (price - 1)))
    supply_curve = plt.plot(price, window.supply_1.get() + (window.supply_el.get() * (price - 1)))
    tax_supply_curve = plt.plot(price, window.supply_1.get() + window.fix_tax.get() + (
                (1 + window.prop_tax.get()) * (window.supply_el.get() * (price - 1))))
    calc.printc()
    plt.show()


def random_plt():
    fig = plt.figure()
    ax = plt.axes()
    ax.set_title('Supply and demand of product X\n')
    ax.set_xlabel('Quantity\n')
    ax.set_ylabel('Price')
    demand_1 = random.uniform(100, 500)
    demand_el = random.uniform(0.1, 0.9)
    supply_1 = random.uniform((demand_1 / 2), (demand_1 / 5))
    supply_el = random.uniform(0.1, 0.9)
    fix_tax = random.uniform(0.5, 10)
    prop_tax = random.uniform(0.01, 0.9)
    price_when_demand_0 = demand_1 / demand_el
    price = np.linspace(1, price_when_demand_0, 100000)
    calc.demand_curve = plt.plot(price, demand_1 - (demand_el * (price - 1)))
    supply_curve = plt.plot(price, supply_1 + (supply_el * (price - 1)))
    tax_supply_curve = plt.plot(price, supply_1 + fix_tax + (
                (1 + prop_tax) * (supply_el * (price - 1))))
    plt.show()
