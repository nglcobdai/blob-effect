# blob-effect

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **License**     | ![LICENSE](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Environment** | ![Ubuntu](https://img.shields.io/badge/-Ubuntu_22.04_LTS-fad9c1.svg?logo=ubuntu&style=flat) <br> ![Docker](https://img.shields.io/badge/-Docker_v26.0.2-0055a4.svg?logo=docker&style=flat) ![Docker Compose](https://img.shields.io/badge/-Docker_Compose_v2.22.0-0055a4.svg?logo=docker&style=flat) <br> ![Python](https://img.shields.io/badge/-Python_3.10-F9DC3E.svg?logo=python&style=flat) ![Poetry](https://img.shields.io/badge/-Poetry-2c2d72.svg?logo=python&style=flat) |
|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## Description

- This software applies a blob effect to images.
  - It randomly positions a specified number of blobs on the input image.
  - The size of each blob is determined randomly within a defined radius range.
- It connects the points using a spline curve, calculated based on a complex formula, to create and render the blob effect.

## Requirements

- Docker and docker-compose are required. The versions are as follows.

  - `Docker`: `v26.0.2`
  - `Docker Compose`: `v2.22.0`

## Demo

|     |            Input            |               Output               |
| :-: | :-------------------------: | :--------------------------------: |
|  1  | ![demo1](./data/demo1.png)  | ![demo1](./output/demo1_blob.png)  |
|  2  | ![demo2](./data/demo2.jpeg) | ![demo2](./output/demo2_blob.jpeg) |

## Getting Started

### 1. Clone Repository

```sh
$ git clone -b v1.1.2 https://github.com/nglcobdai/blob-effect.git
$ cd blob-effect
```

### 2. Create .env

- copy .env.example to .env

```sh
$ cp .env{.example,}
```

### 3. Docker Build & Run

```sh
$ docker-compose build --no-cache
$ docker-compose up -d
$ docker-compose exec project /bin/bash
```

### 4. Run Project

run with `./cfg/demo1.yml`

```sh
$ python3 blob_effect/main.py -c demo1
```

|      Option       | Default | Description                                     |
| :---------------: | :-----: | :---------------------------------------------- |
| `-c` / `--config` | `demo1` | config file path<br>reference `./cfg/demo1.yml` |

- If you want to run with another config file, please prepare it in `./cfg/` directory.
  - Rules for writing config files are [here](./docs/config-rule.md).
- If you want to run with another image file, please prepare it in `./data/` directory.
