# Mendelbrot CPU Stress Test

![header](https://platosrealm.wordpress.com/wp-content/uploads/2018/09/mandel_zoom_08_satellite_antenna.jpg?w=1400)

The **Mandelbrot set** is a famous fractal named after the mathematician Benoît B. Mandelbrot. It's a complex and infinitely detailed shape that is defined by a simple mathematical formula. To create the Mandelbrot set, you take a complex number $c$ and repeatedly apply the function $z=z^2+c$. 

If the result stays bounded (doesn't go to infinity), the point $c$ is part of the Mandelbrot set and is typically colored black. If it doesn't stay bounded, the point is not in the set and is colored differently, usually based on how quickly it escapes to infinity. 

This process creates intricate and beautiful patterns that are self-similar at different scales, meaning you can zoom in indefinitely and see similar structures at every level.

## Significance

The Mandelbrot set is important in mathematics because it is an example of how **simple rules can create incredibly complex and detailed structures**. It has applications in various fields, such as physics, biology, and computer graphics, helping scientists and engineers model complex systems. Historically, the Mandelbrot set was first visualized in the 1980s with the advent of computer graphics, revolutionizing the way people think about mathematical sets and chaos theory. Benoît Mandelbrot's work on fractals has opened up new areas of research and has had a lasting impact on both theoretical and applied mathematics.

### Further Explanations by Experts 

- [Mandelbrot Zoom Sequence](https://www.youtube.com/watch?v=b005iHf8Z3g)
- [The Mandelbrot Set](https://www.youtube.com/watch?v=NGMRB4O922I)
- [What's so special about the Mandelbrot Set?](https://www.youtube.com/watch?v=FFftmWSzgmk)

## This Repository

In this repository, you will find 4 scripts:

- `mandelbrot_image.py`: generates an image of the mandelbrot
- `mandelbrot_video.py`: generates a video or gif of the mandelbrot
- `mandelbrot_image.slurm`: SLURM script to execute `mandelbrot_image.py` on the HPC (64 cores, 8GM RAM)
- `mandelbrot_video.slurm`: SLURM script to execute `mandelbrot_video.py` on the HPC (64 cores, 8GM RAM)

The idea of these scripts it to stress test the CPU of your machines and showing how much quicker the HPC is at complex mathematical processes. Feel free to use it on your computer and/or HPC!

![footer](https://upload.wikimedia.org/wikipedia/commons/2/21/Mandel_zoom_00_mandelbrot_set.jpg)
