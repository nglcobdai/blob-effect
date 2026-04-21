import numpy as np
import pytest
from PIL import Image


@pytest.fixture
def rgb_image():
    rng = np.random.default_rng(seed=0)
    return rng.integers(0, 256, size=(32, 48, 3), dtype=np.uint8)


@pytest.fixture
def rgb_image_path(tmp_path, rgb_image):
    path = tmp_path / "sample.png"
    Image.fromarray(rgb_image, mode="RGB").save(path)
    return path
