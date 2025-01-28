import numpy as np
import matplotlib.pyplot as plt

from metodaEulera import euler_method
from ulepszonaMetodaEulera import improved_euler_method
from metodaRungegoKutty import rk4_numpy
from pomiarBledu import Errorcost
def problem2():
    def dydx(x, y):
        return np.cos(x)+np.sin(x)

    def analytical_solution(x, y0):
        return np.sin(x)-np.cos(x)+1

    equation = r"$\frac{dy}{dx} =cos(x)+sin(x)$"
    solution = r"$y(x) =sin(x)-cos(x)+1$"

    return dydx, analytical_solution, equation, solution

dydx, analytical_solution, equation, solution = problem2()

x0 = 0
y0 =0
h = 0.1
x_end = 2
n = int((x_end - x0) / h)

x_euler, y_euler = euler_method(dydx, x0, y0, h, x_end)
x_improved, y_improved = improved_euler_method(dydx, x0, y0, h, x_end)
x_rk, y_rk = rk4_numpy(dydx, x0, y0, h, n)
x_analytical = np.linspace(x0, x_end, 500)
y_analytical = analytical_solution(x_analytical, y0)
error_costs = Errorcost(dydx, h, x0, x_end, y0, n, analytical_solution)
plt.figure(figsize=(12, 6))
plt.plot(x_euler, y_euler, label=f"Metoda Eulera (h={h})", linestyle='--', color='turquoise',)
plt.plot(x_improved, y_improved, label=f"Ulepszona Metoda Eulera (h={h})", marker='x', linestyle='-.', color='green')
plt.plot(x_analytical, y_analytical, label="Rozwiązanie analityczne", linestyle='--', color='red')
plt.plot(x_rk,y_rk,label=f"Metoda Rungego-Kutty (h={h})", marker='o', linestyle='-',linewidth=0.5)
plt.title("Porównanie metod numerycznych i rozwiązania analitycznego", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.legend(fontsize=10)
plt.grid()

plt.text(
    x_end + 0.2, (max(y_analytical) + min(y_analytical)) / 4*3,
    f"Równanie różniczkowe:\n{equation}\n\nRozwiązanie analityczne:\n{solution}",
    fontsize=12,
    ha='left',
    va='center',
    bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.5')
)
plt.text(
    x_end + 0.15, (max(y_analytical) + min(y_analytical)) / 4,
 f"Metoda Eulera: {error_costs[0]:.4f}\nUlepszona Metoda Eulera: {error_costs[1]:.4f}\nRK: {error_costs[2]:.4f}",
    fontsize=9.5,
    ha='left',
    va='center',
    bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.5')
)
plt.subplots_adjust(right=0.75)

plt.show()
