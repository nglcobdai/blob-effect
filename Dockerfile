FROM ubuntu:22.04

ENV LANG=C.UTF-8 \
    LANGUAGE=en_US \
    PYTHONPATH="/root/workspace/src:$PYTHONPATH" \
    DEBIAN_FRONTEND=noninteractive

# Pythonのインストール
RUN apt-get update && apt-get install -y python3.10 python3-pip \
    && ln -s /usr/bin/python3.10 /usr/bin/python \
    && rm -rf /var/lib/apt/lists/*

# システム依存のライブラリをインストール
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /root/workspace

# Poetryのインストールと依存関係のインストール
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --upgrade poetry

# pyproject.toml、poetry.lock、poetry.tomlをコピーする
COPY pyproject.toml poetry.lock poetry.toml $WORKDIR/

# Clear cache to free up space
RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN poetry install --no-root
