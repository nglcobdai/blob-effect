import random

from tqdm import tqdm

from src.script.blob_effect.blob import Blob


class BlobEffect:
    def __init__(self, config, img) -> None:
        """BlobEffect

        Args:
            config (Dict[*]): 設定ファイル
            img (np.ndarray): 画像
        """
        self.img = img
        self.height, self.width, _ = self.img.shape
        self.config = config

        self.n = self.config.get("blob_num")

        self.blobs = []

    def get_img(self):
        """画像を返す

        Returns:
            np.ndarray: 画像
        """
        return self.img

    def __call__(self):
        """blob effectを実行する"""
        self.setup()
        self.draw()

    def setup(self):
        """blobをセットアップする"""
        for _ in range(self.n):
            pos_x = random.randint(0, self.width - 1)
            pos_y = random.randint(0, self.height - 1)

            color = tuple(int(val) for val in self.img[pos_y, pos_x])

            radius_mn = self.config.get("radius/min", 5)
            radius_mx = self.config.get("radius/max", 30)
            radius = random.randint(radius_mn, radius_mx)

            dense_mn = self.config.get("dense/min", 10)
            dense_mx = self.config.get("dense/max", 50)
            dense = random.randint(dense_mn, dense_mx)

            thickness_mn = self.config.get("thickness/min", 1)
            thickness_mx = self.config.get("thickness/max", 3)
            thickness = random.randint(thickness_mn, thickness_mx)

            self.blobs.append(
                Blob(self.img, pos_x, pos_y, color, radius, dense, thickness)
            )

    def draw(self):
        """blobを描画する"""
        with tqdm(total=self.n) as pbar:
            for _, blob in zip(range(self.n), self.blobs):
                blob()
                pbar.update(1)
