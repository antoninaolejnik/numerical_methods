import numpy as np
import matplotlib.pyplot as plt

from metodaEulera import euler_method
from ulepszonaMetodaEulera import improved_euler_method
def problem1():
    def dydx(x, y):
        return x + y

    def analytical_solution(x, y0):
        return (y0 + 1) * np.exp(x) - x - 1

    equation = r"$\frac{dy}{dx} = x + y$"
    solution = r"$y(x) = (y_0 + 1)e^x - x - 1$"

    return dydx, analytical_solution, equation, solution

dydx, analytical_solution, equation, solution = problem1()

x0 = 0
y0 = 1
h = 0.1
x_end = 2

x_euler, y_euler = euler_method(dydx, x0, y0, h, x_end)
x_improved, y_improved = improved_euler_method(dydx, x0, y0, h, x_end)
x_analytical = np.linspace(x0, x_end, 500)
y_analytical = analytical_solution(x_analytical, y0)

plt.figure(figsize=(12, 6))
plt.plot(x_euler, y_euler, label="Metoda Eulera (h=0.1)", marker='o', linestyle='-')
plt.plot(x_improved, y_improved, label="Ulepszona Metoda Eulera (h=0.1)", marker='x', linestyle='-.', color='green')
plt.plot(x_analytical, y_analytical, label="Rozwiązanie analityczne", linestyle='--', color='red')
plt.title("Porównanie metod numerycznych i rozwiązania analitycznego", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.legend(fontsize=10)
plt.grid()

plt.text(
    x_end + 0.2, (max(y_analytical) + min(y_analytical)) / 2,
    f"Równanie różniczkowe:\n{equation}\n\nRozwiązanie analityczne:\n{solution}",
    fontsize=12,
    ha='left',
    va='center',
    bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.5')
)

plt.subplots_adjust(right=0.75)

plt.show()
