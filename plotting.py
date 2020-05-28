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
    ax.grid(True)
    quantity = np.linspace(window.supply_min.get(), window.demand_max.get(), 100000)
    demand_curve = plt.plot(quantity, (-quantity + window.demand_max.get())/window.demand_el.get()) #azul
    supply_curve = plt.plot(quantity, (quantity - window.supply_min.get())/window.supply_el.get()) #laranja
    tax_supply_curve = plt.plot(quantity, (quantity + (1+window.prop_tax.get()) * (window.fix_tax.get() - window.supply_min.get())/window.supply_el.get())) #verde
    plt.show()


def random_plt():
    fig = plt.figure()
    ax = plt.axes()
    ax.set_title('Supply and demand of product X\n')
    ax.set_xlabel('Quantity\n')
    ax.set_ylabel('Price')
    ax.grid(True)
    demand_max = random.uniform(100, 500)
    demand_el = random.uniform(0.1, 0.9)
    supply_min = random.uniform((demand_max / 2), (demand_max / 5))
    supply_el = random.uniform(0.1, 0.9)
    fix_tax = random.uniform(0.5, 10)
    prop_tax = random.uniform(0.01, 0.9)
    quantity = np.linspace(supply_min, demand_max, 100000)
    demand_curve = plt.plot(quantity, (-quantity + demand_max) / demand_el)  # azul
    supply_curve = plt.plot(quantity, (quantity - supply_min) / supply_el)  # laranja
    tax_supply_curve = plt.plot(quantity, (quantity + (1+prop_tax) * (fix_tax - supply_min) / supply_el))  # verde
    plt.show()
