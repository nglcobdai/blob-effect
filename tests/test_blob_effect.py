import random

import numpy as np

from blob_effect import BlobEffectInfo, RangeComponents
from blob_effect.vision.blob.effect import BlobEffect


def test_blob_effect_output_matches_input_shape_and_dtype():
    random.seed(0)
    np.random.seed(0)

    info = BlobEffectInfo(
        blob_num=3,
        radius=RangeComponents(min=2, max=4),
        thickness=RangeComponents(min=1, max=1),
        is_fill=False,
        is_square=False,
    )
    info.input = np.full((32, 32, 3), 127, dtype=np.uint8)

    BlobEffect.execute(info)

    assert info.output.shape == info.input.shape
    assert info.output.dtype == np.uint8


def test_blob_effect_modifies_image():
    random.seed(1)
    np.random.seed(1)

    info = BlobEffectInfo(
        blob_num=30,
        radius=RangeComponents(min=4, max=6),
        thickness=RangeComponents(min=1, max=2),
        is_fill=True,
        is_square=False,
    )
    # horizontal gradient so each sampled blob color differs from neighbours,
    # making drawn strokes observable.
    gradient = np.tile(np.arange(64, dtype=np.uint8)[None, :, None], (64, 1, 3))
    info.input = gradient.copy()

    BlobEffect.execute(info)

    assert not np.array_equal(info.output, info.input)


def test_blob_effect_with_zero_blobs_is_noop():
    info = BlobEffectInfo(
        blob_num=0,
        radius=RangeComponents(min=1, max=2),
        thickness=RangeComponents(min=1, max=1),
    )
    canvas = np.full((16, 16, 3), 200, dtype=np.uint8)
    info.input = canvas.copy()

    BlobEffect.execute(info)

    assert np.array_equal(info.output, canvas)
