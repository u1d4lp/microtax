# Generate pseudo-random numbers for random plotting
import random

demand_1 = random.uniform(100, 500)
demand_el = random.uniform(0.1, 0.9)

supply_1 = random.uniform((demand_1/2), (demand_1/5))
supply_el = random.uniform(0.1, 0.9)

fix_tax = random.uniform(0.5, 10)
prop_tax = random.uniform(0.01, 0.9)