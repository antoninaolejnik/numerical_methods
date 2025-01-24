import numpy as np
def rk4_numpy(f, t0, y0, h, n):
    t_vals = [t0]
    y_vals = [y0]
    t = t0
    y = y0

    for _ in range(n):
        k1 = f(t, y)
        k2 = f(t + 0.5 * h, y + 0.5 * h * k1)
        k3 = f(t + 0.5 * h, y + 0.5 * h * k2)
        k4 = f(t + h, y + h * k3)

        y += (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        t += h

        t_vals.append(t)
        y_vals.append(y)

    return np.array(t_vals), np.array(y_vals)