import numpy as np
from pydantic import BaseModel, ConfigDict
from blob_effect.bootstrap import logger, messenger
from importlib import import_module


class BaseInfo(BaseModel):
    """Base information"""

    _MODULE = "blob_effect.common.base"
    _CLASS = "BaseEffect"
    _TASK: str = "BaseEffect"
    _MES_INFO_S: dict = {"section": "WARNING", "code": "BLE-W0001"}
    _MES_INFO_E: dict = {"section": "WARNING", "code": "BLE-W0002"}

    _INPUT: np.ndarray = None
    _OUTPUT: np.ndarray = None

    ID: int = 0
    TARGET: int = 0

    model_config = ConfigDict(
        arbitrary_types_allowed=True,  # Allow arbitrary types
        validate_assignment=True,  # Validate assignment
    )

    @property
    def input(self):
        return self._INPUT

    @input.setter
    def input(self, value):
        self._INPUT = value

    @property
    def output(self):
        return self._OUTPUT

    @output.setter
    def output(self, value):
        self._OUTPUT = value

    def execute(self):
        module = getattr(import_module(self._MODULE), self._CLASS)
        return module.execute(self)

    def export(self):
        """Get handler parameters

        Returns:
            Dict: Handler parameters
        """
        data = self.model_dump()
        data.update(
            {
                "TASK": self._TASK,
                "INPUT": self.input.shape if self.input is not None else None,
                "OUTPUT": self.output.shape if self.output is not None else None,
            }
        )
        return data


class BaseEffect:
    """Base class"""

    @classmethod
    def execute(cls, info: BaseInfo):
        """Execute task

        Args:
            info (BaseInfo): Base information

        Returns:
            BaseInfo: Base information
        """
        mes_s = messenger(info._MES_INFO_S.get("section"), info._MES_INFO_S.get("code"))
        mes_e = messenger(info._MES_INFO_E.get("section"), info._MES_INFO_E.get("code"))

        logger.info(mes_s)
        logger.debug(info.export())

        output = cls._execute(info)

        logger.info(mes_e)

        return output

    @staticmethod
    def _execute(info: BaseInfo):
        """Execute task

        Args:
            info (BaseInfo): Base information

        Returns:
            BaseInfo: Base information
        """
        pass
