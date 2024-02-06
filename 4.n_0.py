import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# Modified function definition
def modified_function(n):
    x = 1
    y = 1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            x = x + 1
            y = i + j

    return x, y


# Timing the function for various n values
n_values = list(range(1, 101))  # Adjust the range as needed
times = []

for n in n_values:
    start_time = time.time()
    modified_function(n)
    end_time = time.time()
    elapsed_time = end_time - start_time
    times.append(elapsed_time)


# Fitting a polynomial curve
def poly_func(n, a, b, c):
    return a * n ** 2 + b * n + c


params, _ = curve_fit(poly_func, n_values, times)

 #Plotting the actual data and fitted curve
plt.plot(n_values, times, label='Actual Data', marker='o', linestyle='', markersize=5)
fit_curve = poly_func(np.array(n_values), *params)
plt.plot(n_values, fit_curve, label='Fitted Curve', linestyle='--', color='red')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Execution Time vs n with Fitted Curve')
plt.legend()
plt.grid(True)
plt.show()

# Indicating n_0 on the plot (n_0 = 21)
n_0 = 21
plt.plot(n_values, times, label='Actual Data', marker='o', linestyle='', markersize=5)
plt.plot(n_values, fit_curve, label='Fitted Curve', linestyle='--', color='red')
plt.axvline(x=n_0, color='black', linestyle='--', label=f'n_0 = {n_0}')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Execution Time vs n with n_0 Indicated')
plt.legend()
plt.grid(True)
plt.show()
