from PIL import Image
import numpy as np


def LoadImage(results, cfg):
    """Load image

    Args:
        results (Dict[*]): results
        cfg (Dict[*]): parameter
            {
                "PATH": path
                "MODE": mode
            }
            path (str): image path
            mode (str): image mode (RGB or L) (default: RGB)

    Returns:
        (np.ndarray[H, W, C]): image (RGB or L)
    """
    _ = results
    path = cfg.get("PATH", "/data/demo1.png")
    img = Image.open(path).convert(cfg.get("MODE", "RGB"))
    img = np.array(img)
    return img
