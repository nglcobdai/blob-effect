from blob_effect.common.base import BaseInfo
from pathlib import Path


class BaseIOInfo(BaseInfo):
    """Base IO information"""

    _PATH: str = ""

    def __init__(self, **data):
        super().__init__(**data)
        self._PATH = self._PATH if isinstance(self._PATH, Path) else Path(self._PATH)
