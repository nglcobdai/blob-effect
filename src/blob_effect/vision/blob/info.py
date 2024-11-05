from pydantic import ConfigDict

from blob_effect.common.base import BaseInfo
from blob_effect.common.components import RangeComponents
from blob_effect.vision.blob.blob import Blob


class BlobEffectInfo(BaseInfo):
    _MODULE = "blob_effect.vision.blob.effect"
    _CLASS = "BlobEffect"
    _TASK = "BlobEffect"
    _MES_INFO_S: dict = {"section": "INFO", "code": "BLE-I0009"}
    _MES_INFO_E: dict = {"section": "INFO", "code": "BLE-I0010"}

    _BLOB_NUM: int
    _RADIUS: RangeComponents
    _DENSE: RangeComponents
    _THICKNESS: RangeComponents
    _IS_FILL: bool
    _IS_SQUARE: bool

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        validate_assignment=True,
        extra="allow",  # Allow extra fields
    )

    def __init__(
        self,
        blob_num: int = 100,
        radius: RangeComponents = RangeComponents(min=5, max=30),
        dense: RangeComponents = RangeComponents(min=10, max=50),
        thickness: RangeComponents = RangeComponents(min=1, max=3),
        is_fill: bool = False,
        is_square: bool = False,
        **data,
    ):
        super().__init__(**data)
        self._BLOB_NUM = blob_num
        self._RADIUS = radius
        self._DENSE = dense
        self._THICKNESS = thickness
        self._IS_FILL = is_fill
        self._IS_SQUARE = is_square

        self._blobs = BlobInfo()

    @property
    def blob_num(self):
        return self._BLOB_NUM

    @blob_num.setter
    def blob_num(self, value: int):
        self._BLOB_NUM = value

    @property
    def radius(self):
        return self._RADIUS

    @radius.setter
    def radius(self, value: RangeComponents):
        self._RADIUS = value

    @property
    def dense(self):
        return self._DENSE

    @dense.setter
    def dense(self, value: RangeComponents):
        self._DENSE = value

    @property
    def thickness(self):
        return self._THICKNESS

    @thickness.setter
    def thickness(self, value: RangeComponents):
        self._THICKNESS = value

    @property
    def is_fill(self):
        return self._IS_FILL

    @is_fill.setter
    def is_fill(self, value: bool):
        self._IS_FILL = value

    @property
    def is_square(self):
        return self._IS_SQUARE

    @is_square.setter
    def is_square(self, value: bool):
        self._IS_SQUARE = value

    def export(self):
        data = super().export(exclude={"_blobs"})
        data.update(
            {
                "BLOB_NUM": self._BLOB_NUM,
                "RADIUS": self._RADIUS.export(),
                "DENSE": self._DENSE.export(),
                "THICKNESS": self._THICKNESS.export(),
                "IS_FILL": self._IS_FILL,
                "IS_SQUARE": self._IS_SQUARE,
            }
        )
        return data


class BlobInfo:
    def __init__(self):
        self.blobs = list()

    def __call__(self):
        for blob in self.blobs:
            yield blob

    def append(self, blob: Blob):
        self.blobs.append(blob)
