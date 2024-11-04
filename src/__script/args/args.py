import argparse


def get_args():
    """コマンドライン引数を取得する

    Returns:
        argparse.Namespace: コマンドライン引数
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--config",
        type=str,
        default="demo1",
        help="config file name (default: config)",
    )
    return parser.parse_args()
