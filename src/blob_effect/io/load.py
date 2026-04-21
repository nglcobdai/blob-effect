import numpy as np
from PIL import Image, ImageOps

from blob_effect.common.base import BaseEffect
from blob_effect.io.info import BaseIOInfo


class LoadInfo(BaseIOInfo):

    _MODULE = "blob_effect.io.load"
    _CLASS = "LoadImage"
    _TASK = "LoadImage"
    _MES_INFO_S: dict = {"section": "INFO", "code": "BLE-I0001"}
    _MES_INFO_E: dict = {"section": "INFO", "code": "BLE-I0002"}

    _MODE: str = "RGB"

    def __init__(self, input_path: str, **data):
        super().__init__(**data)
        self._PATH = input_path

    @property
    def mode(self):
        return self._MODE

    @mode.setter
    def mode(self, value):
        self._MODE = value

    @property
    def input_path(self):
        return self._PATH

    @input_path.setter
    def input_path(self, value):
        self._PATH = value

    def export(self):
        """Get handler parameters

        Returns:
            Dict: Handler parameters
        """
        data = super().export()
        data.update({"MODE": self.mode, "INPUT_PATH": self.input_path})
        return data


class LoadImage(BaseEffect):

    @staticmethod
    def _execute(li: LoadInfo):
        """Load image

        Args:
            li (LoadInfo): Load information

        Returns:
            LoadInfo: Load information
        """

        img = Image.open(li.input_path).convert(li.mode)

        # EXIF情報の回転データを考慮して画像を正しい向きで読み込む
        exif = img.getexif()
        if exif and 274 in exif and exif[274] != 1:
            img = ImageOps.exif_transpose(img)

        img = np.array(img)  # (np.ndarray[H, W, C])
        li.output = img

        return li
