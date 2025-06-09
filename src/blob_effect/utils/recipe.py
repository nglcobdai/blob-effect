from uuid import uuid4

from blob_effect.bootstrap import logger


class Recipe:

    def __init__(self, *args):
        self.last_id = None
        self.recipe = dict()
        self._setup(*args)

        logger.debug(f"Recipe: {self.export()}")

    def __call__(self):
        """iterate over the recipe and call the task"""
        for id, info in self.recipe.items():
            yield id, info

    def _setup(self, *args):
        """setup the recipe"""
        for info in args:
            self.id_check(info)
            self.target_check(info, self.recipe)
            self._add(info)
        self.last_id = info.id

    @staticmethod
    def id_check(info):
        if info.id is None:
            _id = str(uuid4())
            info.id, info.uuid = _id, _id
        else:
            info.uuid = f"{info.id}-{str(uuid4())}"

    @staticmethod
    def target_check(info, recipe):
        if info.target is None:
            info.target = list(recipe.values())[-1].id if recipe else None
            info.uuid_target = list(recipe.values())[-1].uuid if recipe else None
        else:
            info.uuid_target = recipe[info.target].uuid

    def _add(self, info):
        self.recipe[info.id] = info

    def export(self):
        return [info.export() for info in self.recipe.values()]

    def content(self):
        """return the content of the recipe"""
        return self.recipe
