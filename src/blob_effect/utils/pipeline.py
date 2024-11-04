from blob_effect.bootstrap import logger, messenger


class Pipeline:

    @staticmethod
    def __call__(recipe):
        logger.info(messenger("INFO", "BLE-I0001"))

        _output = None
        for info in recipe():
            info.input = _output
            _output = Pipeline._call_task(info).output

        logger.info(messenger("INFO", "BLE-I0002"))

    @staticmethod
    def _forward(process):
        pass

    @staticmethod
    def _call_task(info):
        return info.execute()


def pipeline(recipe):
    return Pipeline().__call__(recipe)
