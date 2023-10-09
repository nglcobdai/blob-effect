import os
from pathlib import Path
import numpy as np

from PIL import Image

from script.blob_effect.blob_effect import BlobEffect
from script.blob_effect.preprocess import preprocess


def blob_effect(args, config):
    """blob effectを実行する

    Args:
        args (argparse.Namespace): コマンドライン引数
        config (Dict[*]): 設定ファイル
    """
    root = Path(os.environ["INPUT_DIR"])
    filename = Path(args.img)

    # 画像を読み込む
    path = root / filename
    img = Image.open(path)

    img = preprocess(img)

    img = np.array(img)

    # blobクラスを作成する
    blob_effect_manager = BlobEffect(config, img)

    # blobを描画する
    blob_effect_manager()

    # numpy から PIL に変換する
    output = Image.fromarray(blob_effect_manager.get_img())

    # 画像を保存する
    output_root = Path(os.environ["OUTPUT_DIR"])
    path = str(output_root / filename.stem) + "_blob" + filename.suffix
    output.save(path)
