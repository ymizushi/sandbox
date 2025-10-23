#!/usr/bin/env python3
"""
ステレオビジョンテスト用の画像ペアを生成するスクリプト

左右のカメラ画像をシミュレートした画像ペアを生成します。
"""

from PIL import Image, ImageDraw, ImageFont
import numpy as np


def create_simple_stereo_pair(
    width: int = 640,
    height: int = 480,
    num_objects: int = 5,
    max_disparity: int = 50,
    left_path: str = "stereo_left.png",
    right_path: str = "stereo_right.png"
):
    """
    シンプルなステレオ画像ペアを生成

    Args:
        width: 画像の幅
        height: 画像の高さ
        num_objects: オブジェクトの数
        max_disparity: 最大視差（ピクセル）
        left_path: 左画像の保存パス
        right_path: 右画像の保存パス
    """
    # 左右の画像を生成
    left_img = Image.new('RGB', (width, height), color='white')
    right_img = Image.new('RGB', (width, height), color='white')

    left_draw = ImageDraw.Draw(left_img)
    right_draw = ImageDraw.Draw(right_img)

    np.random.seed(42)

    print(f"ステレオ画像ペアを生成中...")
    print(f"  画像サイズ: {width} x {height}")
    print(f"  オブジェクト数: {num_objects}")

    # 複数のオブジェクトを配置
    for i in range(num_objects):
        # ランダムな位置とサイズ
        x = np.random.randint(max_disparity + 50, width - 100)
        y = np.random.randint(50, height - 100)
        size = np.random.randint(30, 80)

        # 深度に応じた視差（近いほど視差が大きい）
        disparity = np.random.randint(5, max_disparity)

        # ランダムな色
        color = (
            np.random.randint(50, 200),
            np.random.randint(50, 200),
            np.random.randint(50, 200)
        )

        # 左画像にオブジェクトを描画
        left_draw.ellipse(
            [x - size, y - size, x + size, y + size],
            fill=color,
            outline='black',
            width=2
        )

        # 右画像には視差分だけ左にずらして描画
        right_draw.ellipse(
            [x - disparity - size, y - size, x - disparity + size, y + size],
            fill=color,
            outline='black',
            width=2
        )

        print(f"  オブジェクト {i+1}: 位置=({x}, {y}), サイズ={size}, 視差={disparity}")

    # 保存
    left_img.save(left_path)
    right_img.save(right_path)
    print(f"\n左画像を保存: {left_path}")
    print(f"右画像を保存: {right_path}")


def create_textured_stereo_pair(
    width: int = 640,
    height: int = 480,
    left_path: str = "stereo_textured_left.png",
    right_path: str = "stereo_textured_right.png"
):
    """
    テクスチャ付きステレオ画像ペアを生成

    Args:
        width: 画像の幅
        height: 画像の高さ
        left_path: 左画像の保存パス
        right_path: 右画像の保存パス
    """
    np.random.seed(42)

    # ランダムなテクスチャを生成
    texture = np.random.randint(0, 255, (height, width, 3), dtype=np.uint8)

    # 左画像
    left_img = Image.fromarray(texture)

    # 右画像: 深度マップを作成して視差を適用
    right_array = np.zeros_like(texture)

    print(f"テクスチャ付きステレオ画像ペアを生成中...")

    # 簡単な深度マップ（中心ほど手前）
    for y in range(height):
        for x in range(width):
            # 中心からの距離に基づいて視差を計算
            center_x, center_y = width // 2, height // 2
            dist = np.sqrt((x - center_x)**2 + (y - center_y)**2)
            max_dist = np.sqrt(center_x**2 + center_y**2)

            # 視差を計算（中心ほど大きい = 手前）
            disparity = int((1 - dist / max_dist) * 40)

            # 右画像を生成（左にシフト）
            if x - disparity >= 0:
                right_array[y, x] = texture[y, x - disparity]
            else:
                right_array[y, x] = [0, 0, 0]  # 境界は黒

    right_img = Image.fromarray(right_array)

    # 保存
    left_img.save(left_path)
    right_img.save(right_path)
    print(f"左画像を保存: {left_path}")
    print(f"右画像を保存: {right_path}")


def create_geometric_stereo_pair(
    width: int = 640,
    height: int = 480,
    left_path: str = "stereo_geometric_left.png",
    right_path: str = "stereo_geometric_right.png"
):
    """
    幾何学パターンのステレオ画像ペアを生成

    Args:
        width: 画像の幅
        height: 画像の高さ
        left_path: 左画像の保存パス
        right_path: 右画像の保存パス
    """
    left_img = Image.new('RGB', (width, height), color=(200, 200, 200))
    right_img = Image.new('RGB', (width, height), color=(200, 200, 200))

    left_draw = ImageDraw.Draw(left_img)
    right_draw = ImageDraw.Draw(right_img)

    print(f"幾何学パターンのステレオ画像ペアを生成中...")

    # 複数の深度で四角形を配置
    depths = [
        (100, 100, 200, 200, 40, (255, 0, 0)),      # 赤（手前）
        (250, 150, 350, 250, 25, (0, 255, 0)),      # 緑（中間）
        (400, 100, 500, 200, 10, (0, 0, 255)),      # 青（奥）
        (150, 300, 300, 400, 30, (255, 255, 0)),    # 黄（中間手前）
        (350, 280, 480, 380, 15, (255, 0, 255)),    # マゼンタ（中間奥）
    ]

    for x1, y1, x2, y2, disparity, color in depths:
        # 左画像
        left_draw.rectangle([x1, y1, x2, y2], fill=color, outline='black', width=3)

        # 右画像（視差分だけ左にシフト）
        right_draw.rectangle(
            [x1 - disparity, y1, x2 - disparity, y2],
            fill=color,
            outline='black',
            width=3
        )

        depth_name = {40: "手前", 30: "中間手前", 25: "中間", 15: "中間奥", 10: "奥"}
        print(f"  {color}: 視差={disparity}px ({depth_name.get(disparity, '')})")

    # グリッド線を追加（テクスチャとして）
    for x in range(0, width, 40):
        left_draw.line([(x, 0), (x, height)], fill='gray', width=1)
        right_draw.line([(x, 0), (x, height)], fill='gray', width=1)
    for y in range(0, height, 40):
        left_draw.line([(0, y), (width, y)], fill='gray', width=1)
        right_draw.line([(0, y), (width, y)], fill='gray', width=1)

    # 保存
    left_img.save(left_path)
    right_img.save(right_path)
    print(f"左画像を保存: {left_path}")
    print(f"右画像を保存: {right_path}")


def main():
    print("=" * 60)
    print("ステレオビジョンテスト画像生成")
    print("=" * 60)

    # 1. シンプルなオブジェクト
    print("\n[1] シンプルなステレオペア")
    print("-" * 60)
    create_simple_stereo_pair()

    # 2. テクスチャ付き
    print("\n[2] テクスチャ付きステレオペア")
    print("-" * 60)
    create_textured_stereo_pair()

    # 3. 幾何学パターン
    print("\n[3] 幾何学パターンステレオペア")
    print("-" * 60)
    create_geometric_stereo_pair()

    print("\n" + "=" * 60)
    print("完了！以下のコマンドでステレオビジョンを試してください:")
    print("=" * 60)
    print("\n# シンプルなオブジェクト")
    print("uv run python stereo_vision.py stereo_left.png stereo_right.png -o disparity_simple.png --stats")
    print("\n# テクスチャ付き")
    print("uv run python stereo_vision.py stereo_textured_left.png stereo_textured_right.png -o disparity_textured.png")
    print("\n# 幾何学パターン")
    print("uv run python stereo_vision.py stereo_geometric_left.png stereo_geometric_right.png -o disparity_geometric.png --stats")
    print("\n# カラーマップも出力")
    print("uv run python stereo_vision.py stereo_geometric_left.png stereo_geometric_right.png -o disparity.png --color disparity_color.png")


if __name__ == "__main__":
    main()
