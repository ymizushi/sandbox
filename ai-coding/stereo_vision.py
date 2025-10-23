#!/usr/bin/env python3
"""
ステレオビジョン - Sum of Absolute Differences (SAD) プログラム

2つの画像（左カメラ・右カメラ）から視差マップを生成します。
SADを使って対応点を探索し、視差をグレースケールで出力します。
"""

from PIL import Image
import numpy as np
from typing import Tuple
import argparse
from pathlib import Path


def load_stereo_images(left_path: str, right_path: str) -> Tuple[np.ndarray, np.ndarray]:
    """
    ステレオ画像ペアを読み込む

    Args:
        left_path: 左画像のパス
        right_path: 右画像のパス

    Returns:
        (left_gray, right_gray): グレースケール化された画像のタプル
    """
    # 画像を読み込み
    left_img = Image.open(left_path).convert('L')  # グレースケールに変換
    right_img = Image.open(right_path).convert('L')

    # numpy配列に変換
    left_array = np.array(left_img, dtype=np.float32)
    right_array = np.array(right_img, dtype=np.float32)

    # サイズチェック
    if left_array.shape != right_array.shape:
        raise ValueError(
            f"画像サイズが一致しません: "
            f"Left={left_array.shape}, Right={right_array.shape}"
        )

    return left_array, right_array


def compute_sad(left_patch: np.ndarray, right_patch: np.ndarray) -> float:
    """
    Sum of Absolute Differences (SAD) を計算

    Args:
        left_patch: 左画像のパッチ
        right_patch: 右画像のパッチ

    Returns:
        SAD値
    """
    return np.sum(np.abs(left_patch - right_patch))


def compute_disparity_map(
    left_img: np.ndarray,
    right_img: np.ndarray,
    window_size: int = 11,
    max_disparity: int = 64
) -> np.ndarray:
    """
    視差マップを計算

    Args:
        left_img: 左画像（グレースケール）
        right_img: 右画像（グレースケール）
        window_size: マッチングウィンドウのサイズ（奇数）
        max_disparity: 最大視差探索範囲

    Returns:
        視差マップ（numpy配列）
    """
    height, width = left_img.shape
    disparity_map = np.zeros((height, width), dtype=np.float32)

    # ウィンドウの半径
    half_window = window_size // 2

    print(f"視差マップを計算中...")
    print(f"  画像サイズ: {width} x {height}")
    print(f"  ウィンドウサイズ: {window_size} x {window_size}")
    print(f"  最大視差: {max_disparity}")

    # 各ピクセルについて視差を計算
    for y in range(half_window, height - half_window):
        if y % 20 == 0:
            progress = (y - half_window) / (height - 2 * half_window) * 100
            print(f"  処理中: {progress:.1f}%")

        for x in range(half_window, width - half_window):
            # 左画像のパッチを取得
            left_patch = left_img[
                y - half_window:y + half_window + 1,
                x - half_window:x + half_window + 1
            ]

            best_disparity = 0
            min_sad = float('inf')

            # 視差の範囲で探索
            for d in range(max_disparity + 1):
                # 右画像での対応位置
                x_right = x - d

                # 境界チェック
                if x_right - half_window < 0:
                    break

                # 右画像のパッチを取得
                right_patch = right_img[
                    y - half_window:y + half_window + 1,
                    x_right - half_window:x_right + half_window + 1
                ]

                # SADを計算
                sad = compute_sad(left_patch, right_patch)

                # 最小SADを持つ視差を記録
                if sad < min_sad:
                    min_sad = sad
                    best_disparity = d

            disparity_map[y, x] = best_disparity

    print("  完了!")
    return disparity_map


def normalize_disparity_map(disparity_map: np.ndarray) -> np.ndarray:
    """
    視差マップを0-255の範囲に正規化

    Args:
        disparity_map: 視差マップ

    Returns:
        正規化された視差マップ（uint8）
    """
    # 有効な視差値の範囲を取得
    min_disp = np.min(disparity_map)
    max_disp = np.max(disparity_map)

    print(f"\n視差の範囲: {min_disp:.2f} - {max_disp:.2f}")

    if max_disp - min_disp == 0:
        return np.zeros_like(disparity_map, dtype=np.uint8)

    # 0-255に正規化
    normalized = ((disparity_map - min_disp) / (max_disp - min_disp) * 255)
    return normalized.astype(np.uint8)


def save_disparity_map(disparity_map: np.ndarray, output_path: str):
    """
    視差マップをグレースケール画像として保存

    Args:
        disparity_map: 視差マップ
        output_path: 出力パス
    """
    # 正規化
    normalized = normalize_disparity_map(disparity_map)

    # 画像として保存
    img = Image.fromarray(normalized, mode='L')
    img.save(output_path)
    print(f"\n視差マップを保存しました: {output_path}")


def create_colored_disparity_map(disparity_map: np.ndarray, output_path: str):
    """
    視差マップをカラーマップで可視化

    Args:
        disparity_map: 視差マップ
        output_path: 出力パス
    """
    try:
        import matplotlib.pyplot as plt
        import matplotlib
        matplotlib.use('Agg')  # GUIなしで動作

        normalized = normalize_disparity_map(disparity_map)

        plt.figure(figsize=(12, 8))
        plt.imshow(normalized, cmap='jet')
        plt.colorbar(label='Disparity (視差)')
        plt.title('Stereo Vision - Disparity Map')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.tight_layout()
        plt.savefig(output_path, dpi=150)
        plt.close()
        print(f"カラー視差マップを保存しました: {output_path}")
    except ImportError:
        print("警告: matplotlibがインストールされていません。カラーマップはスキップします。")


def compute_depth_statistics(disparity_map: np.ndarray):
    """
    視差マップの統計情報を表示

    Args:
        disparity_map: 視差マップ
    """
    # ゼロでない視差のみを考慮
    valid_disparities = disparity_map[disparity_map > 0]

    if len(valid_disparities) == 0:
        print("\n警告: 有効な視差が見つかりませんでした")
        return

    print("\n視差統計情報:")
    print(f"  平均視差: {np.mean(valid_disparities):.2f}")
    print(f"  中央値: {np.median(valid_disparities):.2f}")
    print(f"  標準偏差: {np.std(valid_disparities):.2f}")
    print(f"  最小値: {np.min(valid_disparities):.2f}")
    print(f"  最大値: {np.max(valid_disparities):.2f}")
    print(f"  有効ピクセル率: {len(valid_disparities) / disparity_map.size * 100:.1f}%")


def main():
    parser = argparse.ArgumentParser(
        description='ステレオビジョン - Sum of Absolute Differences (SAD)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用例:
  # 基本的な使用方法
  python stereo_vision.py left.png right.png -o disparity.png

  # ウィンドウサイズと最大視差を指定
  python stereo_vision.py left.png right.png -o disparity.png -w 15 -d 128

  # カラーマップも出力
  python stereo_vision.py left.png right.png -o disparity.png --color disparity_color.png

  # 統計情報も表示
  python stereo_vision.py left.png right.png -o disparity.png --stats
        """
    )

    parser.add_argument('left', help='左画像のパス')
    parser.add_argument('right', help='右画像のパス')
    parser.add_argument('-o', '--output', required=True,
                        help='出力視差マップのパス')
    parser.add_argument('-w', '--window-size', type=int, default=11,
                        help='マッチングウィンドウサイズ（奇数、デフォルト: 11）')
    parser.add_argument('-d', '--max-disparity', type=int, default=64,
                        help='最大視差探索範囲（デフォルト: 64）')
    parser.add_argument('--color', type=str,
                        help='カラーマップ出力パス（オプション）')
    parser.add_argument('--stats', action='store_true',
                        help='統計情報を表示')

    args = parser.parse_args()

    # ウィンドウサイズが奇数かチェック
    if args.window_size % 2 == 0:
        print("エラー: ウィンドウサイズは奇数である必要があります")
        return 1

    try:
        # ステレオ画像を読み込み
        print(f"画像を読み込み中...")
        print(f"  左画像: {args.left}")
        print(f"  右画像: {args.right}")
        left_img, right_img = load_stereo_images(args.left, args.right)

        # 視差マップを計算
        disparity_map = compute_disparity_map(
            left_img,
            right_img,
            window_size=args.window_size,
            max_disparity=args.max_disparity
        )

        # 統計情報を表示
        if args.stats:
            compute_depth_statistics(disparity_map)

        # グレースケール視差マップを保存
        save_disparity_map(disparity_map, args.output)

        # カラーマップを保存（オプション）
        if args.color:
            create_colored_disparity_map(disparity_map, args.color)

        print("\n処理完了!")
        return 0

    except FileNotFoundError as e:
        print(f"エラー: ファイルが見つかりません: {e}")
        return 1
    except ValueError as e:
        print(f"エラー: {e}")
        return 1
    except Exception as e:
        print(f"エラー: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit(main())
