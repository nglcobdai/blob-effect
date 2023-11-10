from matplotlib import pyplot as plt


def ShowImage(results, cfg):
    key = cfg.get("IMAGE")
    img = results[key]

    plt.title(key)
    plt.imshow(img)

    plt.axis("off")

    plt.show()

    plt.clf()
    plt.close()
