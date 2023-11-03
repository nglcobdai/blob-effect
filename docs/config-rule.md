# コンフィグファイル設定方法

- コンフィグファイルは`YAML`形式で記述する
- 記述のために大きく 2 つのセクションに分けられる
  - `TASK`タグの記述方法
    - タスクのパラメータの設定
  - `Pipeline`の記述方法
    - タスクの実行順序の設定

# タスク一覧

## utils 系

### Load/LoadImage

#### 概要

- `LoadImage` は画像を読み込むタスク

`/data/demo1.png`を RGB 画像として読み込む

#### パラメータ一覧

| パラメータ名 | 説明                 | デフォルト値      | 備考               |
| :----------- | :------------------- | :---------------- | ------------------ |
| `PATH`       | 画像のパス           | `/data/demo1.png` |
| `MODE`       | 画像の読み込みモード | `RGB`             | 選択肢: `RGB`, `L` |

#### 設定例

```yaml
TASK: utils.Load.LoadImage
PARAM:
  PATH: /data/demo1.png
  MODE: RGB
```

---

### Save/SaveImage

#### 概要

- `SaveImage` は画像を保存するタスク

`LoadImage`で読み込んだ画像を`/output/demo1.png`に保存する

#### パラメータ一覧

| パラメータ名 | 説明            | デフォルト値        | 備考 |
| :----------- | :-------------- | :------------------ | ---- |
| `IMAGE`      | 使用画像の`KEY` | ---                 |      |
| `PATH`       | 画像のパス      | `/output/demo1.png` |

#### 設定例

```yaml
TASK: utils.Save.SaveImage
PARAM:
  IMAGE: LoadImage
  PATH: /output/demo1.png
```

---

## vision 系

### Preprocess/Resize

#### 概要

- `Resize` は画像をリサイズするタスク
- リサイズ時の補間は`Image.LANCZOS`を使用
- オリジナル画像が正方形でない場合
  - オリジナルの小さい方の辺の長さを`SIZE`タグに合わせてリサイズ

`LoadImage`で読み込んだ画像を`256x256`にリサイズする

#### パラメータ一覧

| パラメータ名 | 説明               | デフォルト値 | 備考 |
| :----------- | :----------------- | :----------- | ---- |
| `IMAGE`      | 使用画像の`KEY`    | ---          |      |
| `SIZE`       | リサイズ後のサイズ | ---          |      |
| `WIDTH`      | リサイズ後の幅     | 256          |      |
| `HEIGHT`     | リサイズ後の高さ   | 256          |      |

#### 設定例

```yaml
TASK: vision.Preprocess.Resize
PARAM:
  IMAGE: LoadImage
  SIZE:
    WIDTH: 256
    HEIGHT: 256
```

---

### Effect/BlobEffect

#### 概要

- `BlobEffect` は画像に BlobEffect をかけるタスク
- 各パラメータは最小値と最大値の間でランダムに決定される

#### パラメータ一覧

| パラメータ名 | 説明                               | デフォルト値 | 備考                   |
| :----------- | :--------------------------------- | :----------- | ---------------------- |
| `IMAGE`      | 使用画像の`KEY`                    | ---          |                        |
| `BLOB_NUM`   | Blob の数                          | 100          |                        |
| `RADIUS`     | Blob の半径                        | ---          |                        |
| `DENSE`      | 各 Blob 描画のためのプロットの個数 | ---          | 大きいほど描画速度低下 |
| `THICKNESS`  | Blob の太さ                        | ---          |                        |

#### 設定例

- デフォルト設定
  - `LoadImage`で読み込んだ画像に BlobEffect をかける

```yaml
TASK: vision.Effect.BlobEffect
PARAM:
  IMAGE: LoadImage
  BLOB_NUM: 100
  RADIUS:
    MIN: 5
    MAX: 30
  DENSE:
    MIN: 10
    MAX: 50
  THICKNESS:
    MIN: 1
    MAX: 3
```

---

---

# Pipeline の記述方法

## 基本設計

- YAML のリスト形式で実行したいタスクの順番通りに記述する

### 設計例

1. `/data/demo1.png`を RGB 画像として読み込む
2. 読み込んだ画像を`256x256`にリサイズする
3. リサイズした画像を`/output/demo1.png`に保存する

- 上記の設計を実現するためには以下のように記述する

```yaml
- TASK: utils.Load.LoadImage
  PARAM:
    PATH: /data/demo1.png
    MODE: RGB
- TASK: vision.Preprocess.Resize
  PARAM:
    IMAGE: LoadImage
    SIZE:
      WIDTH: 256
      HEIGHT: 256
- TASK: utils.Save.SaveImage
  PARAM:
    IMAGE: Resize
    PATH: /output/demo1.png
```

## 階層設計

- `Pipeline`は階層構造を持つことができる
- `ID`タグを指定することで同じタスクを複数回別タスクとして実行することができる

### 設計例

1. `/data/demo1.png`を RGB 画像として読み込む
2. 読み込んだ画像を`256x256`にリサイズする
3. リサイズした画像に対して BlobEffect をかける
4. 3.で得られた画像に対して別のパラメータで BlobEffect をかける
5. 4.で得られた画像を`/output/demo1.png`に保存する

- 上記の設計を実現するためには以下のように記述する
  - `PROCESS`タグ以下はリスト形式で`TASK`を複数記述することができる
  - `TASK`タグの指定は上位階層のタスク名を省略することができる
  - `ID`タグを指定することで同じタスクを複数回別タスクとして実行することができる
  - `ID`タグが指定されているタスクの結果を参照する場合は`TASK.ID`のように指定する

```yaml
- TASK: utils.Load.LoadImage
  PARAM:
    PATH: /data/demo1.png
    MODE: RGB
- TASK: vision.Preprocess.Resize
  PARAM:
    IMAGE: LoadImage
    SIZE:
      WIDTH: 256
      HEIGHT: 256
- TASK: vision.Effect
  PROCESS:
    - TASK: BlobEffect
      ID: 1
      PARAM:
        IMAGE: Resize
        BLOB_NUM: 100
        RADIUS:
          MIN: 5
          MAX: 30
        DENSE:
          MIN: 10
          MAX: 50
        THICKNESS:
          MIN: 1
          MAX: 3
    - TASK: BlobEffect
      ID: 2
      PARAM:
        IMAGE: BlobEffect.1
        BLOB_NUM: 10
        RADIUS:
          MIN: 20
          MAX: 30
        DENSE:
          MIN: 10
          MAX: 100
        THICKNESS:
          MIN: 5
          MAX: 10
- TASK: utils.Save.SaveImage
  PARAM:
    IMAGE: BlobEffect.2
    PATH: /output/demo1.png
```
