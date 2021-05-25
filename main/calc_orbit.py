import numpy as np

from scipy import optimize

AU = 149597871 # km

def f_full(E, M, e):
    return E - e * np.sin(E) - M


def calc_orbit(
    a_planet, e_planet, inc, periapsis, ascending_node, t_0, dt=500000
):
    """
    Calculate the coordinates of a planet using the semi-major axis and the eccentricity
    """

    # Standard gravitational parameter
    mu_sun = 1.327124400189 * 10 ** 11 # km^3 s^-2

    # Convert Kepler elements to radians
    inclination = np.deg2rad(inc)
    arg_of_periapsis = np.deg2rad(periapsis)
    r_ascending_node = np.deg2rad(ascending_node)

    # Planet specific constants
    period = 2 * np.pi * np.sqrt((a_planet ** 3) / (mu_sun))

    # Initial time values
    steps = int(period / dt)
    t = np.linspace(0, period, num=steps)

    # Compute mean anomaly
    M = np.sqrt((mu_sun) / (a_planet ** 3)) * (t - t_0)

    # Compute eccentric anomaly
    E = optimize.newton(lambda x: f_full(x, M, e_planet), np.full((steps), np.pi))

    # Compute true anomaly
    v = 2 * np.arctan((((1 + e_planet) / (1 - e_planet)) ** 0.5) * np.tan(E / 2))

    # Compute the radius
    r = (a_planet * (1 - e_planet ** 2)) / (1 + e_planet * np.cos(v))

    r_asc_node_cos = np.cos(r_ascending_node)
    r_asc_node_sin = np.sin(r_ascending_node)

    arg_of_periapsis_plus_v = arg_of_periapsis + v
    arg_of_periapsis_plus_v_cos = np.cos(arg_of_periapsis_plus_v)
    arg_of_periapsis_plus_v_sin = np.sin(arg_of_periapsis_plus_v)

    inc_cos = np.cos(inclination)
    inc_sin = np.sin(inclination)

    # Now compute the x,y,z coordinates at each time
    coords = (
        np.array(
            [
                r_asc_node_cos * arg_of_periapsis_plus_v_cos
                - r_asc_node_sin * arg_of_periapsis_plus_v_sin * inc_cos,
                r_asc_node_sin * arg_of_periapsis_plus_v_cos
                + r_asc_node_cos * arg_of_periapsis_plus_v_sin * inc_cos,
                inc_sin * arg_of_periapsis_plus_v_sin,
            ]
        )
        * r
    )

    return coords
