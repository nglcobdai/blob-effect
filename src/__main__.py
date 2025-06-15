from blob_effect import (
    BlobEffectInfo,
    LoadInfo,
    Recipe,
    ResizeInfo,
    SaveInfo,
    pipeline,
    RangeComponents,
)
from blob_effect.bootstrap import logger


def main():
    logger.info("-----------------")
    recipe = Recipe(LoadInfo(input_path="/root/workspace/data/IMG_4686.png"))
    pipeline(recipe)
    file = recipe.content()[recipe.last_id].output
    h, w = file.shape[:2]

    recipe = Recipe(
        LoadInfo(input_path="/root/workspace/data/demo1.png"),
        ResizeInfo(width=256, height=256),
        BlobEffectInfo(
            blob_num=200,
            radius=RangeComponents(min=20, max=25),
            thickness=RangeComponents(min=1, max=1),
            is_fill=True,
            is_square=False,
        ),
        ResizeInfo(width=w, height=h, keep_aspect_ratio=False),
        SaveInfo(output_path="/root/workspace/output/demo1.png"),
    )
    logger.info(recipe.export())

    pipeline(recipe)

    logger.info("-----------------")


if __name__ == "__main__":
    main()
