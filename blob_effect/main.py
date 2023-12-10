from blob_effect.script.args.args import get_args
from blob_effect.script.config import load_config
from blob_effect.script.pipeline import load_pipeline


def main():
    args = vars(get_args())
    config = load_config(args["config"])

    pipeline = load_pipeline(config)
    pipeline()


if __name__ == "__main__":
    main()
