import matplotlib.pyplot as plt
import numpy as np
from charge import Charge


def elec_fieldX(charges, X, Y):
    Ex = 0
    for charge in charges:
        x = charge.x
        y = charge.y
        Ex += charge.q*(X - x)/((X - x)**2 + (Y - y)**2)
    return Ex


def elec_fieldY(charges, X, Y):
    Ey = 0
    for charge in charges:
        x = charge.x
        y = charge.y
        Ey += charge.q*(Y - y)/((X - x)**2 + (Y - y)**2)
    return Ey


def drawField(x, y, step, charges):
    x = np.arange(-x, x, step)
    y = np.arange(-y, y, step)

    X, Y = np.meshgrid(x, y)

    Ex = elec_fieldX(charges, X, Y)
    Ey = elec_fieldY(charges, X, Y)

    fig, ax = plt.subplots(figsize=(6, 6))

    ax.streamplot(X, Y, Ex, Ey)

    ax.set_aspect('equal')
    for charge in charges:
        plot_symbol = '-or' if charge.q > 0 else '-ob'
        ax.plot(charge.x, charge.y, plot_symbol)
    plt.show()
