import matplotlib.pyplot as plt
import numpy as np
import math

# Definicja punktów kontrolnych
control_points = np.array([[0, 0], [3.5, 36], [25, 25], [25, 1.5], [-5,3],[-5,33],[15,11],[-0.5,35],[19.5,15.5],[7,0],[1.5,10.5]])
weights = [1, 6, 4, 2, 3, 4, 2, 1, 5, 4, 1]
for i in range(len(control_points)):
    control_points[i] = control_points[i] * weights[i]

# Funkcja pomocnicza do obliczenia wartości krzywej Béziera dla danego parametru t
def bezier_curve(t, control_points):
    n = len(control_points) - 1
    result = 0
    for i, point in enumerate(control_points):
        result += (
            math.comb(n, i)
            * ((1 - t) ** (n - i))
            * (t ** i)
            * point
        )
    return result

t_values = np.linspace(0, 1, 100)
curve_points = np.array([bezier_curve(t, control_points) for t in t_values])

plt.plot(curve_points[:, 0], curve_points[:, 1], label='Krzywa Béziera')
plt.scatter(control_points[:, 0], control_points[:, 1], c='red', label='Punkty kontrolne')
plt.legend()
plt.title('Krzywa Béziera z punktami kontrolnymi')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.show()

