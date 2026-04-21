import numpy as np
from PIL import Image

from blob_effect import LoadInfo, SaveInfo
from blob_effect.io.load import LoadImage
from blob_effect.io.save import SaveImage


def test_load_image_produces_rgb_ndarray(rgb_image_path, rgb_image):
    info = LoadInfo(input_path=str(rgb_image_path))

    LoadImage.execute(info)

    assert isinstance(info.output, np.ndarray)
    assert info.output.shape == rgb_image.shape
    assert info.output.dtype == np.uint8


def test_save_image_writes_file_readable_by_pillow(tmp_path, rgb_image):
    out_path = tmp_path / "out.png"
    info = SaveInfo(output_path=str(out_path))
    info.input = rgb_image

    SaveImage.execute(info)

    assert out_path.exists()
    loaded = np.array(Image.open(out_path).convert("RGB"))
    assert loaded.shape == rgb_image.shape


def test_save_then_load_roundtrip_preserves_shape(tmp_path, rgb_image):
    out_path = tmp_path / "roundtrip.png"
    save = SaveInfo(output_path=str(out_path))
    save.input = rgb_image
    SaveImage.execute(save)

    load = LoadInfo(input_path=str(out_path))
    LoadImage.execute(load)

    assert load.output.shape == rgb_image.shape
