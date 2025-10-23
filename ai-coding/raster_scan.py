#!/usr/bin/env python3
"""
画像をラスタスキャンするプログラム

ラスタスキャン: 画像を左上から右下へ、行ごとに順番に走査する方法
"""

from PIL import Image
import numpy as np
from typing import Generator, Tuple
import argparse


def raster_scan(image_path: str) -> Generator[Tuple[int, int, Tuple[int, ...]], None, None]:
    """
    画像をラスタスキャンして、各ピクセルの座標とRGB値を順次返す

    Args:
        image_path: 画像ファイルのパス

    Yields:
        (x, y, (r, g, b, ...)): x座標、y座標、ピクセル値のタプル
    """
    # 画像を読み込む
    img = Image.open(image_path)

    # RGBモードに変換
    if img.mode != 'RGB':
        img = img.convert('RGB')

    # numpy配列に変換
    img_array = np.array(img)

    height, width = img_array.shape[:2]

    # ラスタスキャン: 上から下へ、左から右へ
    for y in range(height):
        for x in range(width):
            pixel = tuple(img_array[y, x])
            yield (x, y, pixel)


def visualize_raster_scan(image_path: str, output_path: str = None, step: int = 10):
    """
    ラスタスキャンの様子を可視化する

    Args:
        image_path: 入力画像のパス
        output_path: 出力画像のパス（指定しない場合は表示のみ）
        step: 何ピクセルごとにスキャンラインを表示するか
    """
    img = Image.open(image_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')

    img_array = np.array(img)
    height, width = img_array.shape[:2]

    # スキャンラインを描画
    for y in range(0, height, step):
        img_array[y, :] = [255, 0, 0]  # 赤いライン

    result_img = Image.fromarray(img_array)

    if output_path:
        result_img.save(output_path)
        print(f"スキャンライン可視化画像を保存しました: {output_path}")
    else:
        result_img.show()


def print_pixel_info(image_path: str, max_pixels: int = 20):
    """
    ラスタスキャンの結果を標準出力に表示

    Args:
        image_path: 画像ファイルのパス
        max_pixels: 表示する最大ピクセル数
    """
    print(f"画像をラスタスキャン中: {image_path}")
    print("-" * 60)

    count = 0
    for x, y, pixel in raster_scan(image_path):
        if count >= max_pixels:
            print(f"\n... (最初の{max_pixels}ピクセルのみ表示)")
            break

        print(f"位置({x:4d}, {y:4d}): RGB{pixel}")
        count += 1

    # 画像全体の情報を表示
    img = Image.open(image_path)
    print(f"\n画像サイズ: {img.width} x {img.height}")
    print(f"総ピクセル数: {img.width * img.height:,}")


def calculate_statistics(image_path: str):
    """
    ラスタスキャンしながら画像の統計情報を計算

    Args:
        image_path: 画像ファイルのパス
    """
    r_sum, g_sum, b_sum = 0, 0, 0
    pixel_count = 0

    for x, y, (r, g, b) in raster_scan(image_path):
        r_sum += r
        g_sum += g
        b_sum += b
        pixel_count += 1

    print(f"\n画像統計情報:")
    print(f"  平均 R: {r_sum / pixel_count:.2f}")
    print(f"  平均 G: {g_sum / pixel_count:.2f}")
    print(f"  平均 B: {b_sum / pixel_count:.2f}")
    print(f"  総ピクセル数: {pixel_count:,}")


def main():
    parser = argparse.ArgumentParser(
        description='画像をラスタスキャンするプログラム',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用例:
  # 基本的な使用方法（最初の20ピクセルを表示）
  python raster_scan.py image.jpg

  # より多くのピクセルを表示
  python raster_scan.py image.jpg --max-pixels 100

  # 画像統計情報を計算
  python raster_scan.py image.jpg --stats

  # スキャンラインを可視化
  python raster_scan.py image.jpg --visualize --output scan_lines.jpg
        """
    )

    parser.add_argument('image', help='入力画像のパス')
    parser.add_argument('--max-pixels', type=int, default=20,
                        help='表示する最大ピクセル数（デフォルト: 20）')
    parser.add_argument('--stats', action='store_true',
                        help='画像の統計情報を計算')
    parser.add_argument('--visualize', action='store_true',
                        help='ラスタスキャンラインを可視化')
    parser.add_argument('--output', type=str,
                        help='可視化画像の出力パス')
    parser.add_argument('--step', type=int, default=10,
                        help='スキャンラインの間隔（ピクセル）')

    args = parser.parse_args()

    try:
        # 基本的なピクセル情報の表示
        if not args.visualize:
            print_pixel_info(args.image, args.max_pixels)

        # 統計情報の計算
        if args.stats:
            calculate_statistics(args.image)

        # 可視化
        if args.visualize:
            visualize_raster_scan(args.image, args.output, args.step)

    except FileNotFoundError:
        print(f"エラー: ファイルが見つかりません: {args.image}")
        return 1
    except Exception as e:
        print(f"エラー: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
