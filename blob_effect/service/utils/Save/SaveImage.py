from PIL import Image


def SaveImage(results, cfg):
    img = results[cfg.get("IMAGE")]
    path = cfg.get("PATH", "/output/demo1.png")

    img = Image.fromarray(img)

    img.save(path)
