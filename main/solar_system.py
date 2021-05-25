# Program to draw solar system
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

from plot_orbits import plot_orbits

# -------------------------------------------------------------------------------------------------
# Input parameters
# -------------------------------------------------------------------------------------------------

# Astronomical unit value
AU = 149597871  # km

# List containing all necessary orbital parameters
# Semi-major axis is in km
# Inclination is with respect to the ecliptic
all_planets = [
    # Planets
    # a        e         inc    periapsis ascending anomaly name color
    (57909050, 0.205630, 7.005, 29.124, 48.331, 0, False, 0, 2.2023 * 10 ** 4, "Mercury", "sandybrown"),
    (108209000, 0.006772, 3.39, 54.884, 76.68, 0, False, 0, 3.248599 * 10 ** 5, "Venus", "gold"),
    (149596000, 0.0167086, 0, 114.207, -11.26, 0, False, 0, 3.896004 * 10 ** 5, "Earth", "mediumspringgreen"),
    (227939200, 0.0935, 1.85, 286.50, 49.558, 0, False, 0, 4.282837 * 10 ** 4, "Mars", "tomato"),
    (5.2044 * AU, 0.0489, 1.31, 273.867, 100.464, 0, False, 0, 1.266865 * 10 ** 8, "Jupiter", "moccasin"),
    (9.5826 * AU, 0.0565, 2.49, 339.392, 113.665, 0, False, 0, 3.793119 * 10 ** 7, "Saturn", "navajowhite"),
    (19.2185 * AU, 0.046381, 0.77, 96.998857, 74.006, 0, False, 0, 5.973939 * 10 ** 6, "Uranus", "powderblue"),
    (30.07 * AU, 0.008678, 1.77, 276.336, 131.784, 0, False, 0, 6.836529 * 10 ** 6, "Neptune", "dodgerblue"),
    (198206500, 0.25571, 1.077, 177.68, 316.93, 0, False, 0, 0, "Tesla Roadster", "red"),
    (17.834 * AU, 0.96714, 162.26, 111.33, 58.42, 0, False, 0, 0, "Comet Halley", "dimgray"),
    (186 * AU, 0.995111, 89.430, 282.47, 130.59, 0, False, 0, 0, "Comet Hale Bopp", "lightgray"),
    # Moons
    # a      e       inc    p  as an moon pl  name    color
    (384399, 0.0549, 5.145, 0, 0, 0, True, 2, 3.896004 * 10 ** 5, "Moon", "lightgray"),
    (1882700, 0.0074, 2.017, 0, 0, 0, True, 4, 1.266865 * 10 ** 8, "Callisto", "lightgray"),
    (354759, 0.000016, 129.812, 0, 0, 0, True, 7, 6.836529 * 10 ** 6, "Triton", "lightgray"),
]

plot_orbits(all_planets)