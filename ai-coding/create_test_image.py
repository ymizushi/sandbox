#!/usr/bin/env python3
"""
テスト用の画像を生成するスクリプト
"""

from PIL import Image, ImageDraw, ImageFont
import numpy as np


def create_gradient_image(width: int = 400, height: int = 300, filename: str = "test_gradient.png"):
    """グラデーション画像を作成"""
    img_array = np.zeros((height, width, 3), dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            # 水平グラデーション（赤）
            r = int((x / width) * 255)
            # 垂直グラデーション（緑）
            g = int((y / height) * 255)
            # 青は固定
            b = 128

            img_array[y, x] = [r, g, b]

    img = Image.fromarray(img_array)
    img.save(filename)
    print(f"グラデーション画像を作成しました: {filename}")


def create_checkerboard_image(width: int = 400, height: int = 300,
                               cell_size: int = 50, filename: str = "test_checkerboard.png"):
    """チェッカーボード画像を作成"""
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)

    for y in range(0, height, cell_size):
        for x in range(0, width, cell_size):
            # チェッカーボードパターン
            if ((x // cell_size) + (y // cell_size)) % 2 == 0:
                draw.rectangle([x, y, x + cell_size, y + cell_size], fill='black')

    img.save(filename)
    print(f"チェッカーボード画像を作成しました: {filename}")


def create_numbered_grid(width: int = 400, height: int = 300,
                        cell_size: int = 100, filename: str = "test_grid.png"):
    """番号付きグリッド画像を作成"""
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)

    # グリッド線を描画
    for x in range(0, width, cell_size):
        draw.line([(x, 0), (x, height)], fill='black', width=2)
    for y in range(0, height, cell_size):
        draw.line([(0, y), (width, y)], fill='black', width=2)

    # セル番号を描画
    cell_num = 0
    for y in range(0, height, cell_size):
        for x in range(0, width, cell_size):
            text = str(cell_num)
            # テキストの位置を中央に配置
            bbox = draw.textbbox((0, 0), text)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            text_x = x + (cell_size - text_width) // 2
            text_y = y + (cell_size - text_height) // 2
            draw.text((text_x, text_y), text, fill='red')
            cell_num += 1

    img.save(filename)
    print(f"グリッド画像を作成しました: {filename}")


if __name__ == "__main__":
    print("テスト画像を生成中...")
    create_gradient_image()
    create_checkerboard_image()
    create_numbered_grid()
    print("\n完了！以下のコマンドでラスタスキャンを試してください:")
    print("  python raster_scan.py test_gradient.png")
    print("  python raster_scan.py test_gradient.png --stats")
    print("  python raster_scan.py test_gradient.png --visualize --output scanned.png")
