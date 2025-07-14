from blob_effect.common.base import BaseInfo
import numpy as np


class MaskingInfo(BaseInfo):

    _MODULE = "blob_effect.vision.masking.masking"
    _CLASS = "Masking"
    _TASK = "Masking"
    _MES_INFO_S: dict = {"section": "INFO", "code": "BLE-I0013"}
    _MES_INFO_E: dict = {"section": "INFO", "code": "BLE-I0014"}

    _MASK: np.ndarray = None
    _MASK_PATH: str = None
    _INVERT_MASK: bool = False

    def __init__(self, mask: np.ndarray = None, mask_path: str = None, invert_mask: bool = False, **data):
        super().__init__(**data)
        self._MASK = mask
        self._MASK_PATH = mask_path
        self._INVERT_MASK = invert_mask

    @property
    def mask(self):
        return self._MASK

    @mask.setter
    def mask(self, value):
        self._MASK = value

    @property
    def mask_path(self):
        return self._MASK_PATH

    @mask_path.setter
    def mask_path(self, value):
        self._MASK_PATH = value

    @property
    def invert_mask(self):
        return self._INVERT_MASK

    @invert_mask.setter
    def invert_mask(self, value):
        self._INVERT_MASK = value

    def export(self):
        data = super().export()
        data.update(
            {
                "MASK": self.mask.shape if self.mask is not None else None,
                "MASK_PATH": self.mask_path,
                "INVERT_MASK": self.invert_mask,
            }
        )
        return data
