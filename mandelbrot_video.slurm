#!/bin/bash
#SBATCH --job-name=mandelbrot         # Job name
#SBATCH --partition=standard          # Sets the job priority to standard
#SBATCH --nodes=1                     # Number of nodes
#SBATCH --ntasks=1                    # Number of tasks (processes) per node
#SBATCH --cpus-per-task=64            # Number of CPU cores per task
#SBATCH --mem=8G                      # Memory per node (in this case, 8GB)
#SBATCH --time=02:00:00               # Time limit (HH:MM:SS)
#SBATCH --account=datalab

# Load necessary modules
module load python/3.8                # Load BLAST module (adjust version as needed)

srun python mandelbrot_video.py
