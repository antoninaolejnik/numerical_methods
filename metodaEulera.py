import numpy as np

def euler_method(f, x0, y0, h, x_end):
    x_vals = [x0]
    y_vals = [y0]
    x = x0
    y = y0
    while x < x_end:
        y = y + h * f(x, y)
        x = x + h
        x_vals.append(x)
        y_vals.append(y)
    return np.array(x_vals), np.array(y_vals)


