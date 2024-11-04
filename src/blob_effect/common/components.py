from pydantic import BaseModel, ConfigDict


class BaseComponent(BaseModel):

    _MIN: int
    _MAX: int

    model_config = ConfigDict(validate_assignment=True)

    def __init__(self, min: int = None, max: int = None, **data):
        super().__init__(**data)
        self._MIN = self.min if min is None else min
        self._MAX = self.max if max is None else max

    @property
    def min(self):
        return self._MIN

    @min.setter
    def min(self, value):
        self._MIN = value

    @property
    def max(self):
        return self._MAX

    @max.setter
    def max(self, value):
        self._MAX = value

    def export(self):
        return {"MIN": self.min, "MAX": self.max}


class Radius(BaseComponent):

    _MIN: int = 5
    _MAX: int = 30


class Dense(BaseComponent):

    _MIN: int = 10
    _MAX: int = 50


class Thickness(BaseComponent):

    _MIN: int = 1
    _MAX: int = 3
