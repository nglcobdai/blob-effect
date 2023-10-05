import argparse


def get_args():
    """コマンドライン引数を取得する

    Returns:
        argparse.Namespace: コマンドライン引数
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config",
        type=str,
        default="config",
        help="config file name (default: config)",
    )
    parser.add_argument(
        "--img",
        type=str,
        default="demo.png",
        help="image file name (default: demo.png)",
    )
    return parser.parse_args()
