import numpy as np


def catmull_rom_spline(P0, P1, P2, P3, num_points=100):
    """Catmull-Rom spline

    Args:
        P0 (np.ndarray): control point 0
        P1 (np.ndarray): control point 1
        P2 (np.ndarray): control point 2
        P3 (np.ndarray): control point 3
        num_points (int, optional): number of points. Defaults to 100.

    Description:
        Compute Catmull-Rom spline for given control points.
        P0, P1, P2, and P3 are control points.
        num_points specifies the number of points of the spline curve between P1 and P2.


    Returns:
        np.ndarray: spline points
    """
    points = []

    for t in np.linspace(0, 1, num_points):
        A1 = (1 - t) * P0 + t * P1
        A2 = (1 - t) * P1 + t * P2
        A3 = (1 - t) * P2 + t * P3

        B1 = (1 - t) * A1 + t * A2
        B2 = (1 - t) * A2 + t * A3

        C = (1 - t) * B1 + t * B2

        points.append(C)

    return np.array(points, dtype=np.int32)
