import matplotlib.pyplot as plt
import numpy as np
import calc
import window
import random
from scipy.optimize import fsolve


def show_plt():
    fig = plt.figure()
    ax = plt.axes()
    ax.set_title('Supply and demand of product X\n')
    ax.set_xlabel('Quantity\n')
    ax.set_ylabel('Price')
    max_graph = fsolve(calc.quantity_eq_after_tax, 0.01) * 2
    quantity = np.linspace(1, max_graph, 100000)
    demand_curve = plt.plot()
    supply_curve = plt.plot()
    tax_supply_curve = plt.plot()
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
    max_graph = demand_1 / demand_el
    quantity = np.linspace(1, max_graph, 100000)
    plt.show()
