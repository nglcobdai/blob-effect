import random

from tqdm import tqdm

from copy import deepcopy
from blob_effect.service.vision.Effect.BlobEffect.blob import Blob


class BlobEffect:
    def __init__(self, results, cfg) -> None:
        """BlobEffect

        Args:
            results (Dict[*]): results
                {
                    TASK: image
                }
                TASK (str): task name
                image (np.ndarray[H, W, C]): image (RGB or L)
            cfg (object[Config]): config
                {
                    "IMAGE": TASK
                    "BLOB_NUM": blob_num
                    "RADIUS": radius
                    "DENSE": dense
                    "THICKNESS": thickness
                    "IS_FILL": is_fill
                }
                TASK (str): task name
                blob_num (int): blob num (default: 100)
                radius (Dict[str, int]): radius
                    {
                        "MIN": min
                        "MAX": max
                    }
                    min (int): min radius (default: 5)
                    max (int): max radius (default: 30)
                dense (Dict[str, int]): dense
                    {
                        "MIN": min
                        "MAX": max
                    }
                    min (int): min dense (default: 10)
                    max (int): max dense (default: 50)
                thickness (Dict[str, int]): thickness
                    {
                        "MIN": min
                        "MAX": max
                    }
                    min (int): min thickness (default: 1)
                    max (int): max thickness (default: 3)
                is_fill (bool): fill (default: False)
        """
        self.cfg = cfg
        self.img = deepcopy(results[cfg.get("IMAGE")])
        self.height, self.width, _ = self.img.shape

        self.n = self.cfg.get("BLOB_NUM", 100)
        self.is_fill = self.cfg.get("IS_FILL", False)

        self.blobs = []

    def __call__(self):
        """blob effectを実行する"""
        self.setup()
        self.draw()

        return self.img

    def setup(self):
        """blobをセットアップする"""
        for _ in range(self.n):
            pos_x = random.randint(0, self.width - 1)
            pos_y = random.randint(0, self.height - 1)

            color = tuple(int(val) for val in self.img[pos_y, pos_x])

            radius_mn = self.cfg.get("RADIUS/MIN", 5)
            radius_mx = self.cfg.get("RADIUS/MAX", 30)
            radius = random.randint(radius_mn, radius_mx)

            dense_mn = self.cfg.get("DENSE/MIN", 10)
            dense_mx = self.cfg.get("DENSE/MAX", 50)
            dense = random.randint(dense_mn, dense_mx)

            thickness_mn = self.cfg.get("THICKNESS/MIN", 1)
            thickness_mx = self.cfg.get("THICKNESS/MAX", 3)
            thickness = random.randint(thickness_mn, thickness_mx)

            self.blobs.append(
                Blob(self.img, pos_x, pos_y, color, radius, dense, thickness, self.is_fill)
            )

    def draw(self):
        """blobを描画する"""
        with tqdm(total=self.n) as pbar:
            for _, blob in zip(range(self.n), self.blobs):
                blob()
                pbar.update(1)
