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

all_planets = [
    # a        e         inc periapsis ascending anomaly name
    (57909050, 0.205630, 7.02, 29.124, 48.331, 0, "Mercury", "sandybrown"),
    (108208000, 0.006772, 3.39, 54.884, 76.68, 0, "Venus", "gold"),
    (149696000, 0.0167086, 0, 114.207, -11.26, 0, "Earth", "mediumspringgreen"),
    (227939200, 0.0934, 1.85, 286.50, 49.558, 0, "Mars", "tomato"),
    (5.2044 * AU, 0.0489, 1.31, 273.867, 100.464, 0, "Jupiter", "moccasin"),
    (9.5826 * AU, 0.0565, 2.49, 339.392, 113.665, 0, "Saturn", "navajowhite"),
    (19.2185 * AU, 0.046381, 0.77, 96.998857, 74.006, 0, "Uranus", "powderblue"),
    (30.07 * AU, 0.008678, 1.77, 276.336, 131.784, 0, "Neptune", "dodgerblue"),
    (198206500, 0.25571, 1.077, 177.68, 316.93, 0, "Tesla Roadster", "red"),
    (17.834 * AU, 0.96714, 162.26, 111.33, 58.42, 0, "Comet Halley", "dimgray"),
    (186 * AU, 0.995111, 89.430, 282.47, 130.59, 0, "Comet Hale Bopp", "lightgray"),
]

plot_orbits(all_planets)