import matplotlib.pyplot as plt
import numpy as np
from charge import Charge
from elecfield import drawField

charges = []

# Ask user for charge particle details
n = int(input('Please enter the number of charges to add on the graph: '))
for i in range(n):
    x, y, q = input(
        'Please enter charge particle values in the following format separated by spaces: x position, y position, charge value \n').split()
    Q = Charge(int(x), int(y), int(q))
    charges.append(Q)
drawField(4, 4, 0.2, charges)
