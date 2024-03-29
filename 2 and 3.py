import time
import numpy as np
import matplotlib.pyplot as plt

def f(n):
    x = 1
    for i in range(n):
        for j in range(n):
            x += 1
    return x

def generate_plots(n_values, time_values, coefficients, upper_bound_coefficients, lower_bound_coefficients):
    # Plotting the time vs n graph
    plt.figure()
    plt.plot(n_values, time_values, 'bo-', label='Actual Data', linewidth=2)
    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.title('Time vs n for the given function')

    fitted_curve_values = np.polyval(coefficients, n_values)
    plt.plot(n_values, fitted_curve_values, 'r--', label='Fitted Curve', linewidth=2)
    plt.legend()
    plt.show()

    # Calculate upper and lower bounds
    upper_bound_curve = np.polyval(upper_bound_coefficients, n_values)
    lower_bound_curve = np.polyval(lower_bound_coefficients, n_values)

    # Plotting the upper and lower bounds
    plt.figure()
    plt.plot(n_values, time_values, 'bo-', label='Actual Data', linewidth=2)
    plt.plot(n_values, upper_bound_curve, 'g--', label='Upper Bound', linewidth=1)
    plt.plot(n_values, fitted_curve_values, 'r--', label='Fitted Curve', linewidth=2)
    plt.plot(n_values, lower_bound_curve, 'g--', label='Lower Bound', linewidth=1)
    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.title('Upper and Lower Bounds')
    plt.legend()

    plt.show()

    print("Fitted Curve:", np.poly1d(coefficients))
    print('Big-Theta: Θ(n^2) \n')

    print("Upper Bound (Big-O):", np.poly1d(upper_bound_coefficients))
    print('Big-O: O(n^2) \n')

    print("Lower Bound (Big-Omega):", np.poly1d(lower_bound_coefficients))
    print('Big-Omega: Ω(n^2) \n')

if __name__ == "__main__":
    n_values = np.arange(1, 101)
    time_values = np.zeros_like(n_values, dtype=float)

    for idx, n in enumerate(n_values):
        start_time = time.time()
        f(n)
        end_time = time.time()
        time_values[idx] = end_time - start_time

    coefficients = np.polyfit(n_values, time_values, 2)
    upper_bound_coefficients = 1.1 * coefficients
    lower_bound_coefficients = 0.9 * coefficients

    generate_plots(n_values, time_values, coefficients, upper_bound_coefficients, lower_bound_coefficients)
