import numpy as np
import matplotlib.pyplot as plt


def generate_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    # Create a grid of complex numbers C = x + iy
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y

    # Initialize Z at zero and a mask to track points that haven't escaped
    Z = np.zeros_like(C)
    escape_time = np.zeros(C.shape, dtype=int)
    mask = np.full(C.shape, True, dtype=bool)

    for i in range(max_iter):
        # Update Z only for points that haven't escaped yet
        Z[mask] = Z[mask] * Z[mask] + C[mask]

        # Check for escape: |Z| > 2 is equivalent to Z.real^2 + Z.imag^2 > 4
        escaped = np.abs(Z) > 2

        # Mark newly escaped points and record their iteration count
        new_escape = escaped & mask
        escape_time[new_escape] = i
        mask[escaped] = False

    return escape_time


# Configuration
width, height = 1000, 1000
max_iter = 100
# Standard view of the Mandelbrot set
xmin, xmax = -2.0, 0.5
ymin, ymax = -1.25, 1.25

# Generate and Plot
fractal = generate_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)

plt.figure(figsize=(10, 10))
plt.imshow(fractal, extent=(xmin, xmax, ymin, ymax), cmap='inferno')
plt.colorbar(label='Iterations to escape')
plt.title("Mandelbrot Fractal (2025 Python Implementation)")
plt.xlabel("Re(c)")
plt.ylabel("Im(c)")
plt.show()
