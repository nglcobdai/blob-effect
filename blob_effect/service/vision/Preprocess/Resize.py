from PIL import Image
import numpy as np


def Resize(results, cfg):
    """画像をリサイズする

    Args:
        results (Dict[*]): results
            {
                TASK: image
            }
            TASK (str): task name
            image (np.ndarray[H, W, C]): image (RGB or L)
        cfg (object[Config]): config
            {
                "IMAGE": TASK
                "SIZE": size
            }
            TASK (str): task name
            size (Tuple[int, int]): size (default: (256, 256))

    Returns:
        (np.ndarray[H, W, C]): image (RGB or L)
    """
    img = results[cfg.get("IMAGE")]
    img = Image.fromarray(img)
    width, height = img.size

    size = (cfg.get("SIZE/WIDTH", 256), cfg.get("SIZE/HEIGHT", 256))

    if width == height:
        img = img.resize(size, Image.LANCZOS)
    elif width < height:
        img = img.resize((size[0], round(size[1] * height / width)), Image.LANCZOS)
    else:
        img = img.resize((round(size[0] * width / height), size[1]), Image.LANCZOS)

    return np.array(img)
