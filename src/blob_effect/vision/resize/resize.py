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
        original_width, original_height = img.size
        target_width, target_height = ri.width, ri.height

        if ri.keep_aspect_ratio:
            # 縦横比を保ったままリサイズ
            width_ratio = target_width / original_width
            height_ratio = target_height / original_height

            # より小さい縮小率を使用して指定サイズ内に収める
            resize_ratio = min(width_ratio, height_ratio)

            new_width = int(original_width * resize_ratio)
            new_height = int(original_height * resize_ratio)
        else:
            # 強制的に指定サイズにリサイズ（縦横比無視）
            new_width = target_width
            new_height = target_height

        # リサイズ実行
        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        ri.output = np.array(img)

        return ri
