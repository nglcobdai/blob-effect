ARG python_image_v="python:3.10-buster"
FROM ${python_image_v}

# bashをデフォルトのシェルとして設定
SHELL ["/bin/bash", "-c"]

ENV LANG C.UTF-8
ENV LANGUAGE en_US

WORKDIR /root/workspace

# Poetryのインストールと設定
ENV POETRY_HOME=/opt/poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /opt/poetry/bin/poetry /usr/local/bin/poetry

COPY pyproject.toml poetry.lock poetry.toml $WORKDIR/

ENV PYTHONPATH "/root/workspace/src:$PYTHONPATH"

RUN poetry install --no-root

# 環境変数の設定
COPY .env $WORKDIR/
RUN source $WORKDIR/.env

RUN python -m ipykernel install --user --name python3.10 --display-name "Python 3.10.12"
