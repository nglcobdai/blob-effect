import random
from copy import deepcopy

from tqdm import tqdm

from blob_effect.common.base import BaseEffect
from blob_effect.vision.blob.blob import Blob
from blob_effect.vision.blob.info import BlobEffectInfo


class BlobEffect(BaseEffect):

    @staticmethod
    def _execute(bi: BlobEffectInfo):

        BlobEffect._setup(bi)
        BlobEffect._draw(bi)

        return bi

    @staticmethod
    def _setup(bi: BlobEffectInfo):
        """blobをセットアップする"""
        img = deepcopy(bi.input)
        height, width, _ = img.shape
        radius_mn, radius_mx = bi.radius.min, bi.radius.max
        dense_mn, dense_mx = bi.dense.min, bi.dense.max
        thickness_mn, thickness_mx = bi.thickness.min, bi.thickness.max

        for _ in range(bi.blob_num):
            pos_x = random.randint(0, width - 1)
            pos_y = random.randint(0, height - 1)
            color = tuple(int(val) for val in img[pos_y, pos_x])
            radius = random.randint(radius_mn, radius_mx)
            dense = random.randint(dense_mn, dense_mx)
            thickness = random.randint(thickness_mn, thickness_mx)

            bi._blobs.append(
                Blob(
                    img,
                    pos_x,
                    pos_y,
                    color,
                    radius,
                    dense,
                    thickness,
                    bi.is_fill,
                    bi.is_square,
                )
            )

        bi.output = img

    @staticmethod
    def _draw(bi: BlobEffectInfo):
        """blobを描画する"""
        with tqdm(total=bi.blob_num) as pbar:
            for _, blob in zip(range(bi.blob_num), bi._blobs()):
                blob()
                pbar.update(1)
