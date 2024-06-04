import numpy as np
import matplotlib.pyplot as plt
import time
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

def save_mandelbrot(image, elapsed_time):
    # Get the current date and time
    current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f"mandelbrot_{current_time}_{elapsed_time:.2f}_seconds.png"

    # Save the image
    plt.imshow(image.T, cmap='inferno', extent=[-2, 1, -1.5, 1.5])
    plt.colorbar()
    plt.title('Mandelbrot Set')
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.savefig(filename)
    plt.close()
    print(f"Image saved as {filename}")

if __name__ == "__main__":
    # Parameters
    width, height = 3000, 2000  # Resolution of the image
    x_min, x_max = -2.0, 1.0
    y_min, y_max = -1.5, 1.5
    max_iter = 1000

    # Start the timer
    start_time = time.time()

    # Generate the Mandelbrot set image
    image = generate_mandelbrot_image(width, height, x_min, x_max, y_min, y_max, max_iter)

    # End the timer
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    # Print the time taken
    print(f"Done! The Mandelbrot set took {elapsed_time:.2f} seconds to generate.")

    # Save the Mandelbrot set
    save_mandelbrot(image, elapsed_time)

