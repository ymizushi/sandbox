# 画像処理プログラム集

画像処理とコンピュータビジョンのアルゴリズムを実装したPythonプログラム集です。

## プログラム一覧

1. **ラスタスキャン** - 画像を左上から右下へ順番に走査
2. **ステレオビジョン** - 2つの画像から視差マップを生成（SAD法）

## セットアップ

このプロジェクトは [uv](https://docs.astral.sh/uv/) を使用して依存関係を管理しています。

### 依存関係のインストール

```bash
# uvがインストールされていない場合
curl -LsSf https://astral.sh/uv/install.sh | sh

# 依存関係のインストール
uv sync
```

### 依存パッケージ

- `pillow` - 画像処理ライブラリ
- `numpy` - 数値計算ライブラリ

## ファイル構成

### ラスタスキャン関連
- `raster_scan.py` - 画像ラスタスキャンプログラム
- `create_test_image.py` - テスト用画像生成スクリプト

### ステレオビジョン関連
- `stereo_vision.py` - ステレオビジョン（SAD法）プログラム
- `create_stereo_test_images.py` - ステレオ画像ペア生成スクリプト

### プロジェクト設定
- `pyproject.toml` - プロジェクト設定と依存関係
- `.venv/` - 仮想環境（自動生成）

---

# 1. ラスタスキャン

画像を左上から右下へ、行ごとに順番に走査するプログラムです。

## 使い方

### テスト画像の生成

```bash
uv run python create_test_image.py
```

これにより以下の3つのテスト画像が生成されます：
- `test_gradient.png` - グラデーション画像
- `test_checkerboard.png` - チェッカーボード画像
- `test_grid.png` - 番号付きグリッド画像

### 画像のラスタスキャン

#### 基本的な使用方法（最初の20ピクセルを表示）

```bash
uv run python raster_scan.py test_gradient.png
```

#### より多くのピクセルを表示

```bash
uv run python raster_scan.py test_gradient.png --max-pixels 100
```

#### 画像統計情報を計算

```bash
uv run python raster_scan.py test_gradient.png --stats
```

#### スキャンラインを可視化

```bash
uv run python raster_scan.py test_gradient.png --visualize --output scan_lines.png
```

#### スキャンラインの間隔を変更

```bash
uv run python raster_scan.py test_gradient.png --visualize --output scan_lines.png --step 20
```

## ラスタスキャンとは

ラスタスキャンは、画像やディスプレイを走査する最も基本的な方法です：

```
→→→→→→→→→→
→→→→→→→→→→
→→→→→→→→→→
→→→→→→→→→→
```

- 左上から開始
- 各行を左から右へスキャン
- 行が終わったら次の行へ移動
- 右下で終了

## プログラムの機能

### `raster_scan()` 関数

画像をラスタスキャンして、各ピクセルの座標とRGB値をジェネレータで返します。

```python
for x, y, (r, g, b) in raster_scan("image.jpg"):
    print(f"位置({x}, {y}): RGB({r}, {g}, {b})")
```

### `visualize_raster_scan()` 関数

ラスタスキャンの走査線を赤いラインで可視化します。

### `calculate_statistics()` 関数

ラスタスキャンしながら画像の平均RGB値を計算します。

## 応用例

このプログラムは以下のような用途に応用できます：

- 画像処理アルゴリズムの基礎学習
- ピクセル単位の画像解析
- 画像圧縮アルゴリズムの実装
- コンピュータグラフィックスの学習
- CRTディスプレイの動作原理の理解

## 参考情報

ラスタスキャンは、以下のような場面で使用されています：

- CRTディスプレイの電子ビーム走査
- プリンタの印刷ヘッド移動
- 画像エンコーディング（JPEG、PNGなど）
- ビデオ信号の走査方式

---

# 2. ステレオビジョン

2つのカメラ画像（左・右）から視差マップを生成し、深度情報を取得するプログラムです。Sum of Absolute Differences (SAD) アルゴリズムを使用しています。

## ステレオビジョンとは

ステレオビジョンは人間の両眼視覚を模した技術で、2つの異なる位置から撮影した画像を比較することで、物体までの距離（深度）を推定します。

### 仕組み

1. **視差（Disparity）**: 左右の画像で同じ物体が異なる位置に映る現象
2. **深度推定**: 視差が大きいほど物体は近く、小さいほど遠い
3. **SAD（Sum of Absolute Differences）**: 画像パッチ間の類似度を測定する手法

```
左カメラ     右カメラ
   |           |
   └─────┬─────┘
         |
      視差が発生
         ↓
      物体の深度を推定
```

## 使い方

### テスト用ステレオ画像ペアの生成

```bash
uv run python create_stereo_test_images.py
```

以下の3種類のステレオ画像ペアが生成されます：

1. **シンプルなオブジェクト**
   - `stereo_left.png` / `stereo_right.png`
   - カラフルな円形オブジェクトが複数配置

2. **テクスチャ付き**
   - `stereo_textured_left.png` / `stereo_textured_right.png`
   - ランダムテクスチャで中心が手前の深度マップ

3. **幾何学パターン**
   - `stereo_geometric_left.png` / `stereo_geometric_right.png`
   - 異なる深度の四角形とグリッド

### 視差マップの生成

#### 基本的な使用方法

```bash
uv run python stereo_vision.py stereo_left.png stereo_right.png -o disparity.png
```

#### 統計情報を表示

```bash
uv run python stereo_vision.py stereo_geometric_left.png stereo_geometric_right.png \
  -o disparity_geometric.png --stats
```

#### パラメータを調整

```bash
# ウィンドウサイズを15x15に、最大視差を128に設定
uv run python stereo_vision.py stereo_left.png stereo_right.png \
  -o disparity.png -w 15 -d 128
```

#### カラーマップで可視化

```bash
uv run python stereo_vision.py stereo_geometric_left.png stereo_geometric_right.png \
  -o disparity.png --color disparity_color.png --stats
```

## プログラムの機能

### `compute_sad()` 関数

2つの画像パッチ間のSum of Absolute Differencesを計算します。

```python
sad = np.sum(np.abs(left_patch - right_patch))
```

### `compute_disparity_map()` 関数

各ピクセルについて、最も類似する対応点を探索し、視差マップを生成します。

- **ウィンドウサイズ**: マッチング時のパッチサイズ（デフォルト: 11x11）
- **最大視差**: 探索範囲（デフォルト: 64ピクセル）

### `normalize_disparity_map()` 関数

視差マップを0-255の範囲に正規化してグレースケール画像として出力します。

## パラメータの説明

| パラメータ | 説明 | デフォルト値 | 推奨範囲 |
|-----------|------|------------|---------|
| `--window-size` (`-w`) | マッチングウィンドウのサイズ（奇数） | 11 | 5-21 |
| `--max-disparity` (`-d`) | 最大視差探索範囲 | 64 | 16-128 |

### パラメータ調整のヒント

- **ウィンドウサイズを大きく**: より安定した結果、但し細部が失われる
- **ウィンドウサイズを小さく**: 細部が保たれる、但しノイズが増える
- **最大視差を大きく**: 近い物体も捉えられる、但し計算時間が増える
- **最大視差を小さく**: 高速、但し近い物体の視差が飽和する

## 応用例

このプログラムは以下のような用途に応用できます：

- ロボットの障害物検知
- 自動運転の深度センシング
- 3D再構成
- AR/VRアプリケーション
- 物体までの距離測定

## 出力例

### グレースケール視差マップ

- 明るい領域: 手前の物体（視差が大きい）
- 暗い領域: 奥の物体（視差が小さい）

### カラーマップ（--color オプション）

- 赤/黄色: 手前
- 緑: 中間
- 青: 奥

## 技術的な詳細

### SADアルゴリズム

1. 左画像の各ピクセルについて、周辺のウィンドウ（パッチ）を取得
2. 右画像の同じ高さで、左側の範囲を探索
3. 各位置でSAD値を計算
4. 最小SAD値を持つ位置が対応点
5. 対応点までの距離が視差

### 計算量

- 時間計算量: O(W × H × D × w²)
  - W, H: 画像の幅と高さ
  - D: 最大視差
  - w: ウィンドウサイズ

### 制約

- エピポーラ制約: 対応点は同じ高さ（y座標）にあると仮定
- 左右の画像は正しく校正（キャリブレーション）されている必要がある
- テクスチャのない領域では精度が低下

## 参考情報

ステレオビジョンは以下のような分野で使用されています：

- コンピュータビジョン
- ロボティクス
- 自動運転技術
- 映像制作（3D映画）
- 医療画像処理
