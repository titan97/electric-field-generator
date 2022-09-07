import matplotlib.pyplot as plt
import numpy as np
from charge import Charge
from elecfield import drawField

charges = []

# Ask user for charge particle details

x, y, q = input(
    'Please enter charge particle values in the following format separated by spaces: x_position, y_position, charge_value \n').split()

print("x position: ", x)
print("y position: ", y)
print("charge: ", q)

Q = Charge(int(x), int(y), int(q))
charges.append(Q)
drawField(4, 4, 0.2, charges)
