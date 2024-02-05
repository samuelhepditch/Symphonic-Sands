import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
plate_width = 10  # inches
plate_height = 10  # inches
plate_thickness = 1/16  # inches
sand_grain_size = 0.3  # mm
sand_density = 2.65  # g/cm^3

# Friction characteristics
friction_coefficients = {
    'sand_to_sand_static': 0.55,
    'sand_to_sand_dynamic': 0.35,
    'sand_to_plate_static': 0.45,
    'sand_to_plate_dynamic': 0.25,
}

# Simulation parameters
frequency = 440  # Hz, A4 note as an example
amplitude = 0.01  # Arbitrary units
damping_factor = 0.05  # Arbitrary damping factor for the system
frame_rate = 30  # FPS for the animation
num_sand_grains = 1000  # Number of sand grains

# Initialize sand particles randomly on the plate
sand_particles = np.random.rand(num_sand_grains, 2) * plate_width

def update(frame_num, sand_particles, ax):
    # Placeholder for the update function
    # This is where you would calculate the new positions of the sand particles
    # based on the current state of the system (e.g., vibrations, collisions)
    # For demonstration purposes, we'll just slightly randomize the positions
    sand_particles += (np.random.rand(*sand_particles.shape)-0.5) * 0.1
    ax.clear()
    ax.scatter(sand_particles[:, 0], sand_particles[:, 1], s=sand_grain_size, color='black')
    ax.set_xlim(0, plate_width)
    ax.set_ylim(0, plate_height)
    ax.set_aspect('equal')
    return ax,

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim((0, plate_width))
ax.set_ylim((0, plate_height))

# Animation
ani = animation.FuncAnimation(fig, update, fargs=(sand_particles, ax,),
                              frames=10, interval=1000/frame_rate, blit=False)
plt.show()
