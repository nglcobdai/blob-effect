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

    _ID: str = None
    _TARGET: str = None

    _UUID: str = None
    _UUID_TARGET: str = None

    model_config = ConfigDict(
        arbitrary_types_allowed=True,  # Allow arbitrary types
        validate_assignment=True,  # Validate assignment
    )

    def __init__(self, id: str = None, target: str = None, **data):
        super().__init__(**data)
        self.id = id
        self.target = target

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

    @property
    def id(self):
        return self._ID

    @id.setter
    def id(self, value):
        self._ID = value

    @property
    def target(self):
        return self._TARGET

    @target.setter
    def target(self, value):
        self._TARGET = value

    @property
    def uuid(self):
        return self._UUID

    @uuid.setter
    def uuid(self, value):
        self._UUID = value

    @property
    def uuid_target(self):
        return self._UUID_TARGET

    @uuid_target.setter
    def uuid_target(self, value):
        self._UUID_TARGET = value

    def execute(self):
        module = getattr(import_module(self._MODULE), self._CLASS)
        return module.execute(self)

    def export(self, **kwargs):
        """Get handler parameters

        Returns:
            Dict: Handler parameters
        """
        data = self.model_dump(**kwargs)
        data.update(
            {
                "UUID": self.uuid,
                "UUID_TARGET": self.uuid_target,
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

        logger.debug(info.export())
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
