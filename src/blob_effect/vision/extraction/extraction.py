from rembg import remove
import numpy as np
from blob_effect.common.base import BaseEffect
from blob_effect.vision.extraction.info import ExtractionInfo


class Extraction(BaseEffect):

    @staticmethod
    def _execute(ei: ExtractionInfo):
        """
        入力画像から背景または前景を抽出する

        Args:
            ei (ExtractionInfo): Extraction information

        Returns:
            ExtractionInfo: 抽出結果を含むExtractionInfo
        """
        img = ei.input  # np.ndarray

        if ei.keep_background:
            # 背景のみを保持: 入力画像から前景(人物等)を除去
            mask = remove(img, only_mask=True)
            if mask.ndim == 3:
                mask = mask[..., 0]
            background = img.copy()
            if background.shape[-1] == 4:
                background = background[..., :3]
            background[mask > 128] = 255
            ei.output = background
        else:
            result = remove(img, only_mask=False)
            # 前景のみを保持: rembgの出力をそのまま利用
            if result.shape[-1] == 4:
                alpha = result[..., 3:4] / 255.0
                foreground = result[..., :3] * alpha + 255 * (1 - alpha)
                ei.output = foreground.astype(np.uint8)
            else:
                ei.output = result

        return ei
