
import numpy as np

def improved_euler_method(f, x0, y0, h, x_end):
    x_vals = [x0]
    y_vals = [y0]
    x = x0
    y = y0
    while x < x_end:
        k1 = f(x, y)
        y_pred = y + h * k1
        k2 = f(x + h, y_pred)
        y = y + (h / 2) * (k1 + k2)
        x = x + h
        x_vals.append(x)
        y_vals.append(y)

    return np.array(x_vals), np.array(y_vals)
