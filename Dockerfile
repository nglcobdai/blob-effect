FROM ubuntu:24.04

ENV LANG=C.UTF-8 \
    LANGUAGE=en_US \
    PYTHONPATH="/root/workspace/src:$PYTHONPATH" \
    DEBIAN_FRONTEND=noninteractive \
    PATH="/root/workspace/.venv/bin:$PATH"

# Pythonのインストール
RUN apt-get update && apt-get install -y python3.12 python3-pip python3.12-venv \
    && ln -sf /usr/bin/python3.12 /usr/bin/python \
    && rm -rf /var/lib/apt/lists/*

# システム依存のライブラリをインストール
# git: required by Poetry to install the nglcobdai-utils VCS dependency
# (system-git-client is enabled in poetry.toml).
RUN apt-get update && apt-get install -y \
    git \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /root/workspace

# Poetryのインストールと依存関係のインストール
# Pin Poetry to the version that generated poetry.lock (see lockfile header)
# to keep image builds reproducible.
ARG POETRY_VERSION=2.3.4
RUN apt-get update && apt-get install -y pipx \
    && rm -rf /var/lib/apt/lists/* \
    && pipx install "poetry==${POETRY_VERSION}" \
    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# pyproject.toml、poetry.lock、poetry.tomlをコピーする
COPY pyproject.toml poetry.lock poetry.toml $WORKDIR/

# Clear cache to free up space
RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN poetry install --no-root
