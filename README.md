# blob-effect

![LICENSE](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)

## Description

- This software applies a blob effect to images.
  - It randomly positions a specified number of blobs on the input image.
  - The size of each blob is determined randomly within a defined radius range.
- It connects the points using a spline curve, calculated based on a complex formula, to create and render the blob effect.

## Demo

|     |            Input            |               Output               |
| :-: | :-------------------------: | :--------------------------------: |
|  1  | ![demo1](./data/demo1.png)  | ![demo1](./output/demo1_blob.png)  |
|  2  | ![demo2](./data/demo2.jpeg) | ![demo2](./output/demo2_blob.jpeg) |

## Getting Started

### 1. Clone & Prepare .env

```sh
$ git clone https://github.com/nglcobdai/blob-effect.git
$ cd blob-effect
```

### 2. Create .env

- copy .env.example to .env

```sh
$ cp .env{.example,}
```

### 3. Docker Build & Run

```sh
docker-compose build --no-cache
docker-compose up -d
docker-compose exec project-blob-effect bash
```

### 4. Run Project

- run with `./cfg/demo1.yml`

  ```sh
  python3 src/main.py -c demo1
  ```

  |      Option       | Default | Description                                     |
  | :---------------: | :-----: | :---------------------------------------------- |
  | `-c` / `--config` | `demo1` | config file path<br>reference `./cfg/demo1.yml` |
