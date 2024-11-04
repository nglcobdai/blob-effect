from blob_effect.common.base import BaseInfo


class ResizeInfo(BaseInfo):

    _MODULE = "blob_effect.vision.resize.resize"
    _CLASS = "Resize"
    _TASK = "Resize"
    _MES_INFO_S: dict = {"section": "INFO", "code": "BLE-I0007"}
    _MES_INFO_E: dict = {"section": "INFO", "code": "BLE-I0008"}

    _WIDTH: int = 256
    _HEIGHT: int = 256

    def __init__(self, width: int, height: int, **data):
        super().__init__(**data)
        self._WIDTH = width
        self._HEIGHT = height

    @property
    def width(self):
        return self._WIDTH

    @width.setter
    def width(self, value):
        self._WIDTH = value

    @property
    def height(self):
        return self._HEIGHT

    @height.setter
    def height(self, value):
        self._HEIGHT = value

    def export(self):
        data = super().export()
        data.update({"WIDTH": self.width, "HEIGHT": self.height})
        return data
