from blob_effect import (
    BlobEffectInfo,
    ExtractionInfo,
    LoadInfo,
    MaskingInfo,
    RangeComponents,
    Recipe,
    ResizeInfo,
    SaveInfo,
    pipeline,
)
from blob_effect.bootstrap import logger


def main():
    logger.info("-----------------")
    logger.info("Starting blob-effect demo")

    # Check if the main demo image exists, otherwise use existing demo1.png
    main_image_path = "/root/workspace/data/IMG_4686.png"
    demo_image_path = "/home/runner/work/blob-effect/blob-effect/data/demo1.png"

    try:
        recipe = Recipe(LoadInfo(input_path=main_image_path))
        pipeline(recipe)
        file = recipe.content()[recipe.last_id].output
        h, w = file.shape[:2]
        logger.info(f"Loaded main image: {main_image_path}")
    except:
        # Fallback to demo image
        recipe = Recipe(LoadInfo(input_path=demo_image_path))
        pipeline(recipe)
        file = recipe.content()[recipe.last_id].output
        h, w = file.shape[:2]
        logger.info(f"Loaded demo image: {demo_image_path}")

    # Original blob effect demo
    logger.info("Running blob effect demo")
    recipe = Recipe(
        LoadInfo(input_path=demo_image_path),
        ResizeInfo(width=256, height=256),
        ExtractionInfo(keep_background=False),
        BlobEffectInfo(
            blob_num=500,
            radius=RangeComponents(min=20, max=25),
            thickness=RangeComponents(min=1, max=1),
            is_fill=False,
            is_square=False,
        ),
        ResizeInfo(width=w, height=h, keep_aspect_ratio=True),
        SaveInfo(output_path="/home/runner/work/blob-effect/blob-effect/output/demo_blob.png"),
    )
    logger.info(recipe.export())
    pipeline(recipe)

    # NEW: Masking demo with circular mask
    logger.info("Running masking demo with circular mask")
    recipe = Recipe(
        LoadInfo(input_path=demo_image_path),
        ResizeInfo(width=256, height=256),
        MaskingInfo(mask_path="/home/runner/work/blob-effect/blob-effect/data/circle_mask.png"),
        SaveInfo(output_path="/home/runner/work/blob-effect/blob-effect/output/demo_circle_masked.png"),
    )
    logger.info(recipe.export())
    pipeline(recipe)

    # NEW: Masking demo with rectangular mask (inverted)
    logger.info("Running masking demo with inverted rectangular mask")
    recipe = Recipe(
        LoadInfo(input_path=demo_image_path),
        ResizeInfo(width=256, height=256),
        MaskingInfo(mask_path="/home/runner/work/blob-effect/blob-effect/data/rect_mask.png", invert_mask=True),
        SaveInfo(output_path="/home/runner/work/blob-effect/blob-effect/output/demo_rect_masked_inverted.png"),
    )
    logger.info(recipe.export())
    pipeline(recipe)

    logger.info("All demos completed successfully!")
    logger.info("-----------------")


if __name__ == "__main__":
    main()
