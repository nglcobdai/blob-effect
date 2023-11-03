from importlib import import_module
from blob_effect.script.config import Config


class Pipeline:
    def __init__(self, cfg):
        self.cfg = cfg
        self.pipeline = list()
        self.results = dict()

    def __call__(self):
        self._load_pipeline(self.cfg)
        self._call_task()

    def _load_pipeline(self, cfg, module_path="blob_effect.service"):
        if isinstance(cfg, list):
            for process in cfg:
                self._load_pipeline(process, module_path)
        elif isinstance(cfg, dict):
            module_path = f"{module_path}.{cfg['TASK']}"
            if "PARAM" in cfg:
                self._load_task(cfg, module_path)
            else:
                self._load_pipeline(cfg["PROCESS"], module_path)
        else:
            raise TypeError(f"Invalid type: {type(cfg)}")

    def _load_task(self, cfg, module_path):
        task = module_path.split(".")[-1]
        _pipeline = {
            "module_path": module_path,
            "name": task,
            "id": cfg.get("ID", None),
            "param": cfg.get("PARAM", dict()),
        }
        self.pipeline.append(_pipeline)

    def _call_task(self):
        results = dict()
        for process in self.pipeline:
            name = process["name"]
            id = process["id"]
            module_path = process["module_path"]
            param = process["param"]
            module = import_module(module_path)
            func = getattr(module, name)
            _name = name if id is None else f"{name}.{id}"
            results[_name] = func(results, Config(param))

        return results
