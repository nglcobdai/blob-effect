from PIL import Image

from blob_effect.common.base import BaseEffect
from blob_effect.io.info import BaseIOInfo


class SaveInfo(BaseIOInfo):

    _MODULE = "blob_effect.io.save"
    _CLASS = "SaveImage"
    _TASK = "SaveImage"
    _MES_INFO_S: dict = {"section": "INFO", "code": "BLE-I0001"}
    _MES_INFO_E: dict = {"section": "INFO", "code": "BLE-I0002"}

    def __init__(self, output_path: str, **data):
        super().__init__(**data)
        self._PATH = output_path

    @property
    def output_path(self):
        return self._PATH

    @output_path.setter
    def output_path(self, value):
        self._PATH = value

    def export(self):
        """Get handler parameters

        Returns:
            Dict: Handler parameters
        """
        data = super().export()
        data.update({"OUTPUT_PATH": self.output_path})
        return data


class SaveImage(BaseEffect):

    @staticmethod
    def _execute(si: SaveInfo):
        """Save image

        Args:
            si (SaveInfo): Save information

        Returns:
            SaveInfo: Save information
        """

        img, path = si.input, si.output_path

        img = Image.fromarray(img)
        img.save(path)

        return si
