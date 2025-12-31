import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 1. Configuration
width, height = 800, 800
max_iter = 100  # Number of color steps in the loop
xmin, xmax = -2.0, 0.5
ymin, ymax = -1.25, 1.25

# 2. Pre-calculate Mandelbrot Set (Escape Times)
def get_mandelbrot_data(w, h, m):
    x = np.linspace(xmin, xmax, w)
    y = np.linspace(ymin, ymax, h)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    Z = np.zeros_like(C)
    escape_time = np.zeros(C.shape, dtype=float)
    mask = np.full(C.shape, True, dtype=bool)

    for i in range(m):
        Z[mask] = Z[mask] * Z[mask] + C[mask]
        escaped = np.abs(Z) > 2
        new_escape = escaped & mask
        escape_time[new_escape] = i
        mask[escaped] = False
    return escape_time

fractal_data = get_mandelbrot_data(width, height, max_iter)

# 3. Setup Looping Animation
fig, ax = plt.subplots(figsize=(8, 8))
plt.subplots_adjust(left=0, right=1, bottom=0, top=1) # Remove borders
img = ax.imshow(fractal_data, cmap='twilight_shifted', animated=True)
ax.axis('off')

def update(frame):
    # Shift colors using frame number + modulo for a seamless loop
    # frame increments indefinitely in FuncAnimation
    shifted_data = (fractal_data + frame) % max_iter
    img.set_array(shifted_data)
    return [img]

# repeat=True ensures the animation restarts once it hits 'frames'
# interval=30 provides a smooth 33 FPS experience
ani = animation.FuncAnimation(fig, update, frames=max_iter,
                              interval=30, blit=True, repeat=True)

plt.show()
