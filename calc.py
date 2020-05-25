import tkinter as tk
import window
import plotting
from scipy.optimize import fsolve


def quantity_eq_before_tax(price):
    return (window.demand_1.get() - (window.demand_el.get() * (price - 1))) - (window.supply_1.get() + (window.supply_el.get() * (price - 1)))


def quantity_eq_after_tax(price):
    return (window.demand_1.get() - (window.demand_el.get() * (price - 1))) - (window.supply_1.get() + window.fix_tax.get() + ((1 + window.prop_tax.get()) * (window.supply_el.get() * (price - 1))))


def price_eq_before_tax():
    return


def printc():
    q_eq_b_tax = fsolve(quantity_eq_before_tax, 0.01)
    q_eq_a_tax = fsolve(quantity_eq_after_tax, 0.01)
    #g0 = fsolve(price_eq_before_tax, 0.01)