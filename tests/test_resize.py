import numpy as np

from blob_effect import ResizeInfo
from blob_effect.vision.resize.resize import Resize


def _make_image(h, w):
    return np.zeros((h, w, 3), dtype=np.uint8)


def test_resize_without_aspect_ratio_uses_exact_size():
    info = ResizeInfo(width=40, height=30, keep_aspect_ratio=False)
    info.input = _make_image(100, 200)

    Resize.execute(info)

    assert info.output.shape == (30, 40, 3)


def test_resize_with_aspect_ratio_fits_within_target():
    info = ResizeInfo(width=50, height=50, keep_aspect_ratio=True)
    info.input = _make_image(100, 200)  # aspect 2:1 landscape

    Resize.execute(info)

    h, w = info.output.shape[:2]
    assert w <= 50 and h <= 50
    # landscape input → width bound hit, height scaled proportionally
    assert w == 50
    assert h == 25


def test_resize_preserves_dtype():
    info = ResizeInfo(width=16, height=16, keep_aspect_ratio=False)
    info.input = _make_image(32, 32)

    Resize.execute(info)

    assert info.output.dtype == np.uint8
