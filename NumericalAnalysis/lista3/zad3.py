import numpy as np
import matplotlib.pyplot as plt
# Polynomial
def polynomial(arg, x_list):
    result = 1
    for x in x_list:
        result *= (arg - x)
    return result

# Chebyshev nodes in the interval [-1, 1]
def chebyshev_nodes(n):
    return np.cos((2 * np.arange(1, n + 2) - 1) * np.pi / (2 * (n + 1)))

# Equidistant nodes in the interval [-1, 1]
def equidistant_nodes(n):
    return np.linspace(-1, 1, n + 1)

def results_in_range_4_20():
    # Prepare plots for different n values
    for i in range(4,21):
        n = i
        x_values = np.linspace(-1, 1, 1000)  # For a smoother plot

        # Plot for Chebyshev nodes
        y_chebyshev = [polynomial(arg, chebyshev_nodes(n)) for arg in x_values]
        plt.plot(x_values, y_chebyshev, label=f'Chebyshev, n={n}', linestyle=':')

        # Plot for equidistant nodes
        y_equidistant = [polynomial(arg, equidistant_nodes(n)) for arg in x_values]
        plt.plot(x_values, y_equidistant, label=f'Equidistant, n={n}')

        # Add labels and legend
        plt.xlabel('x')
        plt.ylabel('p(x)')
        plt.legend()
        plt.title('Comparison of polynomials for Chebyshev and equidistant nodes')
        plt.show()

results_in_range_4_20()
