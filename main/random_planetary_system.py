# Program to draw solar system
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random

from generate_random_planet_names import generate_random_planet_names
from plot_orbits import plot_orbits

def random_color():
    rgb=[random.randint(0, 255)/255, random.randint(0, 255)/255, random.randint(0, 255)/255]
    return tuple(rgb)

# -------------------------------------------------------------------------------------------------
# Input parameters
# -------------------------------------------------------------------------------------------------

# Astronomical unit value
AU = 149597871  # km

amount_of_planets = random.randint(3,20)

all_planets = []
planet_names = generate_random_planet_names(amount_of_planets)

for i in list(range(amount_of_planets)):
    planet = (random.uniform(0, 30 * AU), random.uniform(0,1), random.uniform(0, 180), random.uniform(0, 360), random.uniform(0, 360), 0, planet_names[i], random_color())
    all_planets.append(planet)

plot_orbits(all_planets)