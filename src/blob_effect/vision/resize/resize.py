from PIL import Image
import numpy as np
from blob_effect.common.base import BaseEffect
from blob_effect.vision.resize.info import ResizeInfo


class Resize(BaseEffect):

    @staticmethod
    def _execute(ri: ResizeInfo):
        """画像をリサイズする

        Args:
            ri (ResizeInfo): Resize information

        Returns:
            (np.ndarray[H, W, C]): image (RGB or L)
        """
        img = ri.input
        img = Image.fromarray(img)
        width, height = img.size

        size = (ri.width, ri.height)

        if width == height:
            img = img.resize(size, Image.LANCZOS)
        elif width < height:
            img = img.resize((size[0], round(size[1] * height / width)), Image.LANCZOS)
        else:
            img = img.resize((round(size[0] * width / height), size[1]), Image.LANCZOS)

        ri.output = np.array(img)

        return ri
