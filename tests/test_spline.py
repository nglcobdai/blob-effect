import numpy as np

from blob_effect.vision.blob.spline import catmull_rom_spline


def test_catmull_rom_spline_returns_requested_point_count():
    p = np.array([0.0, 0.0])
    q = np.array([1.0, 0.0])
    r = np.array([2.0, 1.0])
    s = np.array([3.0, 1.0])

    out = catmull_rom_spline(p, q, r, s, num_points=25)

    assert out.shape == (25, 2)
    assert out.dtype == np.int32


def test_catmull_rom_spline_starts_at_p0_and_ends_at_p3():
    p0 = np.array([0.0, 0.0])
    p1 = np.array([5.0, 10.0])
    p2 = np.array([15.0, 10.0])
    p3 = np.array([20.0, 0.0])

    out = catmull_rom_spline(p0, p1, p2, p3, num_points=50)

    assert np.array_equal(out[0], p0.astype(np.int32))
    assert np.array_equal(out[-1], p3.astype(np.int32))
