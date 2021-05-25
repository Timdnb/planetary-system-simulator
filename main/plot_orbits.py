import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# import timeit

from calc_orbit import calc_orbit, AU

# -------------------------------------------------------------------------------------------------
# Support functions
# -------------------------------------------------------------------------------------------------

def plot_orbits(all_planets):
    def plot_orbit_and_return_point(lst_x, lst_y, lst_z, moon, planet, clr, ax):
        """
        Plot the orbit of the planet and make a point at the start location (will be used later to animate)
        """
        if moon == False:
            ax.plot(lst_x, lst_y, lst_z, color=clr, label=planet)

        (point,) = ax.plot(lst_x[0], lst_y[0], lst_z[0], color=clr, marker="o")

        return point


    def update(frame_number, planet_points, x_coords, y_coords, z_coords):
        """
        Updating function, to be repeatedly called by the animation of the planet orbit
        """
        for index, planet_point in enumerate(planet_points):
            # Set x and y coordinate
            planet_point.set_data(
                x_coords[index][frame_number % len(x_coords[index])],
                y_coords[index][frame_number % len(y_coords[index])],
            )
            # Set z coordinate
            planet_point.set_3d_properties(
                z_coords[index][frame_number % len(z_coords[index])]
            )

        return (planet_points,)


    # print(
    #     timeit.timeit(
    #         lambda: calc_orbit(
    #             all_planets[0][0],
    #             all_planets[0][1],
    #             all_planets[0][2],
    #             all_planets[0][3],
    #             all_planets[0][4],
    #             8,
    #             all_planets[0][7],
    #         ),
    #         number=5,
    #     )
    #     / 5 * 1000
    # )

    # -------------------------------------------------------------------------------------------------
    # Setup of plotting
    # -------------------------------------------------------------------------------------------------

    # Plotting parameters
    plt.style.use("dark_background")
    fig = plt.figure(figsize=(8, 8))
    ax = plt.axes(projection="3d")

    # Add the Sun to the plot
    ax.plot(0, 0, 0, color="darkorange", marker="o")

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
        )

        # If the planet is a moon, add the coordinates of the moon's orbit the the coordinates of the planet it is orbiting
        if planet[6] == True:
            moon_x = []
            moon_y = []
            moon_z = []
            for i in list(range(len(list_of_x_coords[planet[7]]))):
                moon_x.append(x[i%len(x)-1] + list_of_x_coords[planet[7]][i])
                moon_y.append(y[i%len(y)-1] + list_of_y_coords[planet[7]][i])
                moon_z.append(z[i&len(z)-1] + list_of_z_coords[planet[7]][i])
            x = moon_x
            y = moon_y
            z = moon_z

        list_of_x_coords.append(x)
        list_of_y_coords.append(y)
        list_of_z_coords.append(z)

        list_of_planet_points.append(plot_orbit_and_return_point(x, y, z, planet[6], planet[8], planet[9], ax))

    # -------------------------------------------------------------------------------------------------
    # Animate orbits
    # -------------------------------------------------------------------------------------------------

    # Create animation with 1ms interval, which is repeated, using the planet point coordinates
    ani = FuncAnimation(
        fig,
        lambda frame: update(
            frame,
            list_of_planet_points,
            list_of_x_coords,
            list_of_y_coords,
            list_of_z_coords,
        ),
        interval=1,
        blit=False,
        repeat=True,
    )

    # -------------------------------------------------------------------------------------------------
    # Finalize and show plot
    # -------------------------------------------------------------------------------------------------

    ax.set_xlim3d([-35 * AU, 35 * AU])
    ax.set_ylim3d([-35 * AU, 35 * AU])
    ax.set_zlim3d([-35 * AU, 35 * AU])

    plt.axis("off")

    ax.legend(loc="upper right")
    plt.tight_layout()

    plt.show()