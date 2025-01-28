import numpy as np
from metodaEulera import euler_method
from ulepszonaMetodaEulera import improved_euler_method
from metodaRungegoKutty import rk4_numpy


def Errorcost(f, h, x0, x_end, y0, n, analytical_solution):
    Cost_euler = n
    Cost_improved = 2 * Cost_euler
    Cost_rk = 4 * Cost_euler
    v1 = []
    v2 = []
    v3 = []
    A = []
    x = np.linspace(x0, x_end, n)
    for i in range(n):
        v1.append(np.abs(euler_method(f, x0, y0, h, x_end)[1][i] - analytical_solution(x[i], y0)))
        v2.append(np.abs(improved_euler_method(f, x0, y0, h, x_end)[1][i] - analytical_solution(x[i], y0)))
        v3.append(np.abs(rk4_numpy(f, x0, y0, h, n)[1][i] - analytical_solution(x[i], y0)))
    A.append(max(v1) * Cost_euler)
    A.append(max(v2) * Cost_improved)
    A.append(max(v3) * Cost_rk)
    return A