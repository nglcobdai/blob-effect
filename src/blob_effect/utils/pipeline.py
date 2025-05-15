from blob_effect.bootstrap import logger, messenger


class Pipeline:

    @staticmethod
    def __call__(recipe):
        logger.info(messenger("INFO", "BLE-I0001"))

        Pipeline._execute(recipe)

        logger.info(messenger("INFO", "BLE-I0002"))

    @staticmethod
    def _execute(recipe):
        for _, info in recipe():
            Pipeline._setup(recipe, info)
            info.execute()

    @staticmethod
    def _setup(recipe, info):
        for _id, _info in recipe():
            if _id == info.target:
                info.input = _info.output
                break


def pipeline(recipe):
    return Pipeline().__call__(recipe)
