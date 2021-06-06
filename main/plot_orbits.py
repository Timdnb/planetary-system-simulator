"""
This program plots the orbits using the coordinates calculated in calc_orbit.py
"""
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

from calc_orbit import calc_orbit, AU

# -------------------------------------------------------------------------------------------------
# Support functions
# -------------------------------------------------------------------------------------------------

def plot_orbits(all_planets, ms=20):
    def plot_orbit_and_return_point(lst_x, lst_y, lst_z, moon, planet, clr, ax):
        """
        Plot the orbit of the planet and make a point at the start location (will be used later to animate)
        """
        if moon == False:
            ax.plot(lst_x, lst_y, lst_z, color=clr, label=planet)
            (point,) = ax.plot(lst_x[0], lst_y[0], lst_z[0], color=clr, marker="o", markersize=5)
        else:
            (point,) = ax.plot(lst_x[0], lst_y[0], lst_z[0], color=clr, marker="o", markersize=2)

        return point


    def update(frame_number, planet_points, x_coords, y_coords, z_coords, planets):
        """
        Updating function, to be repeatedly called by the animation of the planet orbit
        """
        for index, planet_point in enumerate(planet_points):
            moon_dx = 0
            moon_dy = 0
            moon_dz = 0

            # If the planet is a moon, add the coordinates of the moon's orbit the the coordinates of the planet it is orbiting
            if planets[index][6] == True:

                moon_dx = x_coords[planets[index][7]][frame_number % len(x_coords[planets[index][7]])]
                moon_dy = y_coords[planets[index][7]][frame_number % len(y_coords[planets[index][7]])]
                moon_dz = z_coords[planets[index][7]][frame_number % len(z_coords[planets[index][7]])]

            # Set x and y coordinate
            planet_point.set_data(
                x_coords[index][frame_number % len(x_coords[index])] + moon_dx,
                y_coords[index][frame_number % len(y_coords[index])] + moon_dy,
            )
            # Set z coordinate
            planet_point.set_3d_properties(
                z_coords[index][frame_number % len(z_coords[index])] + moon_dz
            )

        return planet_points


    # -------------------------------------------------------------------------------------------------
    # Setup of plotting
    # -------------------------------------------------------------------------------------------------

    # Plotting parameters
    plt.style.use("dark_background")
    fig = plt.figure(figsize=(8, 8))
    ax = plt.axes(projection="3d")

    # Add the Sun to the plot
    ax.plot(0, 0, 0, color="darkorange", marker="o", markersize=7)

    # -------------------------------------------------------------------------------------------------
    # Calculate planet orbits and plot the orbits
    # -------------------------------------------------------------------------------------------------

    # List that contains all points that will be animated
    list_of_planet_points = []

    # Lists that contain x and y coords for all planets
    list_of_x_coords = []
    list_of_y_coords = []
    list_of_z_coords = []

    for planet in all_planets:
        x, y, z = calc_orbit(
            planet[0],
            planet[1],
            planet[2],
            planet[3],
            planet[4],
            planet[5],
            planet[6],
            planet[8],
        )

        list_of_x_coords.append(x)
        list_of_y_coords.append(y)
        list_of_z_coords.append(z)

        list_of_planet_points.append(plot_orbit_and_return_point(x, y, z, planet[6], planet[9], planet[10], ax))

    # -------------------------------------------------------------------------------------------------
    # Animate orbits
    # -------------------------------------------------------------------------------------------------

    # Create animation with interval in ms (20 standard; variable in function), which is repeated, using the planet point coordinates
    ani = FuncAnimation(
        fig,
        lambda frame: update(
            frame,
            list_of_planet_points,
            list_of_x_coords,
            list_of_y_coords,
            list_of_z_coords,
            all_planets
        ),
        interval=ms,
        blit=False,
        repeat=True,
    )

    # -------------------------------------------------------------------------------------------------
    # Finalize and show plot
    # -------------------------------------------------------------------------------------------------

    lst_semi_major_ax =[]
    for i in range(len(all_planets)):
        lst_semi_major_ax.append(all_planets[i][0])
        max_dist = 1.1* max(lst_semi_major_ax)

    ax.set_xlim3d([-max_dist, max_dist])
    ax.set_ylim3d([-max_dist, max_dist])
    ax.set_zlim3d([-max_dist, max_dist])

    plt.axis("off")

    ax.legend(loc="upper right")
    plt.tight_layout()

    plt.show()