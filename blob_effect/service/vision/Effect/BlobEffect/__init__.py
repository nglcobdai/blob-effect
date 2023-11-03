from blob_effect.service.vision.Effect.BlobEffect.blob_effect import (
    BlobEffect as _BlobEffect,
)


def BlobEffect(results, cfg):
    """BlobEffect"""
    return _BlobEffect(results, cfg)()
