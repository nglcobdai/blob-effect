from blob_effect.common.base import BaseInfo


class ExtractionInfo(BaseInfo):

    _MODULE = "blob_effect.vision.extraction.extraction"
    _CLASS = "Extraction"
    _TASK = "Extraction"
    _MES_INFO_S: dict = {"section": "INFO", "code": "BLE-I0011"}
    _MES_INFO_E: dict = {"section": "INFO", "code": "BLE-I0012"}

    _KEEP_BACKGROUND: bool = False

    def __init__(self, keep_background: bool = False, **data):
        super().__init__(**data)
        self._KEEP_BACKGROUND = keep_background

    @property
    def keep_background(self):
        return self._KEEP_BACKGROUND

    @keep_background.setter
    def keep_background(self, value):
        self._KEEP_BACKGROUND = value

    def export(self):
        data = super().export()
        data.update(
            {
                "KEEP_BACKGROUND": self.keep_background,
            }
        )
        return data
