import matplotlib.pyplot as plt
import numpy as np
import math

def kaijo(n):
    if n == 0:
        return 1
    elif n > 0:
        return kaijo(n - 1) * n

def my_sin(x, k):
    result = np.zeros_like(x, dtype=float)
    
    for i in range(0, k):
        index = 2 * i + 1

        mul = x ** index
        sign = (-1) ** i
        dev = kaijo(index)

        result += sign * mul / dev

    return result

# Generate x values
x_values = np.linspace(0,  np.pi, 1000)

# True sin(x) values
true_sin_values = np.sin(x_values)

# Approximations with different k values
for k in [1,3,5]:
    approx_sin_values = my_sin(x_values, k)

    # Absolute error
    absolute_error = np.abs(true_sin_values - approx_sin_values)

    # Plot the absolute error
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, absolute_error, label=f'Absolute Error (k={k})', color='red')
    
    # Add labels, title, and legend
    plt.title(f'Absolute Error between sin(x) and Custom Sin Approximation (k={k})')
    plt.xlabel('x')
    plt.ylabel('Absolute Error')
    plt.legend()
    plt.grid(True)
    plt.show()
