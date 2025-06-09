from blob_effect import (
    BlobEffectInfo,
    LoadInfo,
    Recipe,
    ResizeInfo,
    SaveInfo,
    pipeline,
)
from blob_effect.bootstrap import logger


def main():
    logger.info("-----------------")
    recipe = Recipe(
        LoadInfo(id="01", input_path="/root/workspace/data/demo1.png"),
        ResizeInfo(width=100, height=100),
        BlobEffectInfo(
            target="01",
            blob_num=100,
            is_fill=True,
            is_square=True,
        ),
        SaveInfo(output_path="/root/workspace/output/demo1.png"),
    )
    logger.info(recipe.export())

    pipeline(recipe)

    logger.info("-----------------")


if __name__ == "__main__":
    main()
