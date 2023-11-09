from matplotlib import pyplot as plt


def ShowImage(results, cfg):
    img = results[cfg.get("IMAGE")]
    title = cfg.get("TITLE", None)

    plt.title(title)
    plt.imshow(img)

    plt.axis("off")

    plt.show()

    plt.clf()
    plt.close()
