from PIL import Image


def preprocess(img, size=(256, 256)):
    """画像の前処理を行う

    Args:
        img (_type_): _description_
        size (tuple, optional): _description_. Defaults to (256, 256).

    Returns:
        _type_: _description_
    """
    img = resize(img, size)
    return img


def resize(img, size=(256, 256)):
    """画像をリサイズする

    Args:
        img (_type_): _description_
        size (tuple, optional): _description_. Defaults to (256, 256).

    Returns:
        _type_: _description_
    """
    width, height = img.size

    if width == height:
        return img.resize(size, Image.LANCZOS)
    elif width < height:
        return img.resize((size[0], round(size[1] * height / width)), Image.LANCZOS)
    else:
        return img.resize((round(size[0] * width / height), size[1]), Image.LANCZOS)
