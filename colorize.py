import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 1. Generate Static Mandelbrot Data
def get_mandelbrot(width, height, max_iter):
    x = np.linspace(-2.0, 0.5, width)
    y = np.linspace(-1.25, 1.25, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    Z = np.zeros_like(C)
    escape_time = np.zeros(C.shape, dtype=float)
    mask = np.full(C.shape, True, dtype=bool)

    for i in range(max_iter):
        Z[mask] = Z[mask] * Z[mask] + C[mask]
        escaped = np.abs(Z) > 2
        new_escape = escaped & mask
        escape_time[new_escape] = i
        mask[escaped] = False
    return escape_time

# Configuration
width, height, max_iter = 600, 600, 80
fractal_data = get_mandelbrot(width, height, max_iter)

# 2. Setup Animation
fig, ax = plt.subplots(figsize=(8, 8))
# Initial plot
img = ax.imshow(fractal_data, cmap='inferno', animated=True)
ax.axis('off')

def update(frame):
    # Shift colors by adding the frame number to the escape times
    # Using modulo (%) keeps the values within the colormap range
    shifted_data = (fractal_data + frame) % max_iter
    img.set_array(shifted_data)
    return [img]

# Create animation: 100 frames, 50ms delay between frames
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

plt.show()
