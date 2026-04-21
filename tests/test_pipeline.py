import numpy as np
from PIL import Image

from blob_effect import LoadInfo, Recipe, ResizeInfo, SaveInfo, pipeline


def test_pipeline_load_resize_save(tmp_path, rgb_image_path):
    out_path = tmp_path / "out.png"

    recipe = Recipe(
        LoadInfo(input_path=str(rgb_image_path)),
        ResizeInfo(width=16, height=16, keep_aspect_ratio=False),
        SaveInfo(output_path=str(out_path)),
    )

    pipeline(recipe)

    assert out_path.exists()
    saved = np.array(Image.open(out_path).convert("RGB"))
    assert saved.shape == (16, 16, 3)


def test_pipeline_threads_output_into_next_input(tmp_path, rgb_image_path):
    load = LoadInfo(input_path=str(rgb_image_path))
    resize = ResizeInfo(width=8, height=8, keep_aspect_ratio=False)

    recipe = Recipe(load, resize)
    pipeline(recipe)

    # resize.input was populated from load.output during pipeline execution
    assert resize.input is not None
    assert np.array_equal(resize.input, load.output)
    assert resize.output.shape == (8, 8, 3)
