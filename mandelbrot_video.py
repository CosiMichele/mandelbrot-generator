import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from multiprocessing import Pool, cpu_count
from datetime import datetime

def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def compute_row(args):
    width, y, x_min, x_max, y_min, y_max, max_iter = args
    row = np.empty(width)
    r1 = np.linspace(x_min, x_max, width)
    y0 = y_min + (y / (height - 1)) * (y_max - y_min)
    for i in range(width):
        row[i] = mandelbrot(r1[i] + 1j*y0, max_iter)
    return row

def generate_mandelbrot_image(width, height, x_min, x_max, y_min, y_max, max_iter):
    args = [(width, y, x_min, x_max, y_min, y_max, max_iter) for y in range(height)]
    with Pool(processes=cpu_count()) as pool:
        result = pool.map(compute_row, args)
    return np.array(result)

def update_image(frame, width, height, max_iter, ims, zoom, x_center, y_center):
    zoom_factor = zoom ** frame
    x_min = x_center - 1.5 / zoom_factor
    x_max = x_center + 1.5 / zoom_factor
    y_min = y_center - 1 / zoom_factor
    y_max = y_center + 1 / zoom_factor
    image = generate_mandelbrot_image(width, height, x_min, x_max, y_min, y_max, max_iter)
    ims.set_array(image.T)
    return ims,

if __name__ == "__main__":
    # Parameters
    width, height = 800, 600  # Resolution of the image
    max_iter = 1000
    zoom = 1.1  # Zoom factor for each frame
    num_frames = 100  # Number of frames in the video
    x_center, y_center = -0.5, 0  # Center of the zoom

    # Create the figure and axis
    fig, ax = plt.subplots()
    ax.set_title('Mandelbrot Set')
    ax.set_xlabel('Re')
    ax.set_ylabel('Im')

    # Generate the initial image
    initial_image = generate_mandelbrot_image(width, height, -2.0, 1.0, -1.5, 1.5, max_iter)
    ims = ax.imshow(initial_image.T, cmap='inferno', extent=[-2, 1, -1.5, 1.5])
    plt.colorbar(ims, ax=ax)

    # Create animation
    ani = animation.FuncAnimation(fig, update_image, frames=num_frames, fargs=(width, height, max_iter, ims, zoom, x_center, y_center), interval=100, blit=True)

    # Save the video
    current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f"mandelbrot_zoom_{current_time}.mp4"
    try:
        ani.save(filename, writer='ffmpeg', fps=10)
        print(f"Video saved as {filename}")
    except ValueError:
        filename = f"mandelbrot_zoom_{current_time}.gif"
        ani.save(filename, writer='pillow', fps=10)
        print(f"Animation saved as {filename}")

