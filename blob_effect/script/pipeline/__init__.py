from .pipeline import Pipeline


def load_pipeline(config):
    """パイプラインを読み込む

    Args:
        config (Dict[*]): 設定ファイル

    Returns:
        Pipeline: パイプライン
    """
    return Pipeline(config)
