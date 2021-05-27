# This version will simulate the solar system which is NOT to scale
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

from plot_orbits import plot_orbits

# -------------------------------------------------------------------------------------------------
# Input parameters
# -------------------------------------------------------------------------------------------------

# Astronomical unit value
AU = 149597871  # km

# List containing all necessary orbital parameters (these are NOT the correct values)
# Semi-major axis is in km
# Inclination is with respect to the ecliptic
# For every row: 
#   semi-major axis | eccentricity | inclinaton | arg. of periapsis | long. of asc. node | time of perihelion passage | moon yes/no | list no. of planet that moon orbits | mu | name | color 
all_planets = [
    # ------------------------- Planets -------------------------
    (0.1*AU, 0.205630, 7.005, 29.124, 48.331, 0, False, 0, 2.2023 * 10 ** 4, "Mercury", "sandybrown"),
    (0.2*AU, 0.006772, 3.39, 54.884, 76.68, 0, False, 0, 3.248599 * 10 ** 5, "Venus", "gold"),
    (0.3*AU, 0.0167086, 0, 114.207, -11.26, 0, False, 0, 3.896004 * 10 ** 5, "Earth", "mediumspringgreen"),
    (0.4*AU, 0.0935, 1.85, 286.50, 49.558, 0, False, 0, 4.282837 * 10 ** 4, "Mars", "tomato"),
    (0.6*AU, 0.0489, 1.31, 273.867, 100.464, 0, False, 0, 1.266865 * 10 ** 8, "Jupiter", "moccasin"),
    (0.8*AU, 0.0565, 2.49, 339.392, 113.665, 0, False, 0, 3.793119 * 10 ** 7, "Saturn", "navajowhite"),
    (1.0*AU, 0.046381, 0.77, 96.998857, 74.006, 0, False, 0, 5.973939 * 10 ** 6, "Uranus", "powderblue"),
    (1.2*AU, 0.008678, 1.77, 276.336, 131.784, 0, False, 0, 6.836529 * 10 ** 6, "Neptune", "dodgerblue"),
    # ------------------------- Moons -------------------------
    (0.04*AU, 0.0549, 5.145, 0, 0, 0, True, 2, 3.896004 * 10 ** 10, "Moon", "lightgray"),
    (0.08*AU, 0.0074, 2.017, 0, 0, 0, True, 4, 1.266865 * 10 ** 11, "Callisto", "lightgray"),
    (0.08*AU, 0.000016, 129.812, 0, 0, 0, True, 7, 6.836529 * 10 ** 10, "Triton", "lightgray"),
    # ----------------------------------------------------------------------------------------------------
    # Cool example of moons (put dt=5000000, make all previous lines comments and uncomment the next 5)
    # (30.07 * AU, 0.008678, 1.77, 276.336, 131.784, 0, False, 0, 6.836529 * 10 ** 6, "Neptune", "dodgerblue"),
    # (4 * AU, 0.000016, 0, 0, 0, 0, True, 0, 6.836529 * 10 ** 10, "Test Moon 1", "lightgray"),
    # (4 * AU, 0.000016, 45, 0, 90, 0, True, 0, 6.836529 * 10 ** 10, "Test Moon 2", "lightgray"),
    # (4 * AU, 0.000016, 90, 0, 180, 0, True, 0, 6.836529 * 10 ** 10, "Test Moon 3", "lightgray"),
    # (4 * AU, 0.000016, 135, 0, 270, 0, True, 0, 6.836529 * 10 ** 10, "Test Moon 4", "lightgray"), 
]

plot_orbits(all_planets)