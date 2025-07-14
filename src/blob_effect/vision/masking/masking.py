from PIL import Image
import numpy as np
import cv2
from blob_effect.common.base import BaseEffect
from blob_effect.vision.masking.info import MaskingInfo


class Masking(BaseEffect):

    @staticmethod
    def _execute(mi: MaskingInfo):
        """指定したマスクを元にマスキングされた画像を取得する

        Args:
            mi (MaskingInfo): Masking information

        Returns:
            MaskingInfo: マスキング結果を含むMaskingInfo
        """
        img = mi.input  # np.ndarray

        # Load mask from path if provided, otherwise use mask directly
        if mi.mask_path is not None:
            mask = np.array(Image.open(mi.mask_path))
        elif mi.mask is not None:
            mask = mi.mask
        else:
            raise ValueError("Either mask or mask_path must be provided")

        # Convert mask to grayscale if needed
        if mask.ndim == 3:
            mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

        # Resize mask to match input image size
        if mask.shape[:2] != img.shape[:2]:
            mask = cv2.resize(mask, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_NEAREST)

        # Normalize mask to 0-255 range
        if mask.dtype != np.uint8:
            mask = ((mask - mask.min()) / (mask.max() - mask.min()) * 255).astype(np.uint8)

        # Invert mask if requested
        if mi.invert_mask:
            mask = 255 - mask

        # Convert mask to 0-1 range for blending
        mask_normalized = mask.astype(np.float32) / 255.0

        # Apply mask to image
        if img.ndim == 3:  # Color image
            # Expand mask to match image channels
            mask_expanded = np.expand_dims(mask_normalized, axis=2)
            mask_expanded = np.repeat(mask_expanded, img.shape[2], axis=2)

            # Apply mask (masked areas become black, unmasked areas remain original)
            masked_img = img.astype(np.float32) * mask_expanded
            mi.output = masked_img.astype(np.uint8)
        else:  # Grayscale image
            masked_img = img.astype(np.float32) * mask_normalized
            mi.output = masked_img.astype(np.uint8)

        return mi
