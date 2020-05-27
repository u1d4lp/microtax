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
    quantity = np.linspace(window.supply_1.get(), window.demand_1.get(), 100000)
    demand_curve = plt.plot(quantity, (-quantity + window.demand_1.get())/window.demand_el.get()) #azul
    supply_curve = plt.plot(quantity, (quantity - window.supply_1.get())/window.supply_el.get()) #laranja
    tax_supply_curve = plt.plot(quantity, (quantity + window.prop_tax.get() * (window.fix_tax.get() - window.supply_1.get())/window.supply_el.get())) #verde
    plt.show()


def random_plt():
    fig = plt.figure()
    ax = plt.axes()
    ax.set_title('Supply and demand of product X\n')
    ax.set_xlabel('Quantity\n')
    ax.set_ylabel('Price')
    ax.grid(True)
    demand_1 = random.uniform(100, 500)
    demand_el = random.uniform(0.1, 0.9)
    supply_1 = random.uniform((demand_1 / 2), (demand_1 / 5))
    supply_el = random.uniform(0.1, 0.9)
    fix_tax = random.uniform(0.5, 10)
    prop_tax = random.uniform(0.01, 0.9)
    quantity = np.linspace(0, window.demand_1.get(), 100000)
    demand_curve = plt.plot(quantity, (-quantity + window.demand_1.get()) / window.demand_el.get())
    # supply_curve =
    # tax_supply_curve =
    plt.show()
