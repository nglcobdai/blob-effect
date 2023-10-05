from src.script.utils.args import get_args
from src.script.config import load_config
from src.script.blob_effect import blob_effect


def main():
    args = get_args()
    config = load_config(args.config)

    blob_effect(args, config)


if __name__ == "__main__":
    main()
