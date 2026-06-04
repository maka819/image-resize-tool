import os
import glob
import argparse
from PIL import Image

def process_all_images(input_dir="inputs", output_dir="dist", mode="resize"):
    """
    指定されたフォルダ内の画像をすべてスキャンし、指定モードでWebP画像を一括生成する
    """
    # サポートする拡張子
    extensions = ("*.jpg", "*.jpeg", "*.png", "*.bmp")
    
    # 入力・出力ディレクトリの準備
    if not os.path.exists(input_dir):
        print(f"⚠️ 入力フォルダ '{input_dir}' が見つかりません。作成してください。")
        return
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # フォルダ内の全画像を取得
    target_files = []
    for ext in extensions:
        target_files.extend(glob.glob(os.path.join(input_dir, ext)))

    if not target_files:
        print("📭 処理対象の画像が見つかりませんでした。")
        return

    print(f"🚀 {len(target_files)} 件の処理を開始します...")

    for file_path in target_files:
        if mode == "resize":
            generate_store_webp_images(file_path, output_dir)
        elif mode == "original":
            convert_original_webp(file_path, output_dir)

def generate_store_webp_images(input_path, output_dir):
    """
    (既存のロジック) 1枚の画像から2サイズのWebPを生成
    """
    try:
        with Image.open(input_path) as img:
            base_name = os.path.splitext(os.path.basename(input_path))[0]
            sizes = {
                "ultra": (2560, 1440), # WQHD/4K向け
                "high": (1600, 900),   # @2x
                "standard": (800, 450) # 1x
            }

            for key, size in sizes.items():
                # 16:9クロップ & リサイズ処理
                target_ratio = size[0] / size[1]
                current_ratio = img.width / img.height
                
                temp_img = img.copy()
                if current_ratio > target_ratio:
                    new_width = int(img.height * target_ratio)
                    left = (img.width - new_width) / 2
                    temp_img = temp_img.crop((left, 0, left + new_width, img.height))
                elif current_ratio < target_ratio:
                    new_height = int(img.width / target_ratio)
                    top = (img.height - new_height) / 2
                    temp_img = temp_img.crop((0, top, img.width, top + new_height))

                temp_img = temp_img.resize(size, Image.Resampling.LANCZOS)

                if key == "ultra":
                    suffix = "full"
                elif key == "high":
                    suffix = "@2x"
                else:
                    suffix = ""
                output_path = os.path.join(output_dir, f"{base_name}{suffix}.webp")
                
                temp_img.save(output_path, "WEBP", quality=90)
                print(f"  ∟ ✅ {output_path}")

    except Exception as e:
        print(f"  ∟ ❌ {input_path} の処理中にエラー: {e}")

def convert_original_webp(input_path, output_dir):
    """
    1枚の画像をリサイズせずに元のサイズのままWebPに変換
    """
    try:
        with Image.open(input_path) as img:
            base_name = os.path.splitext(os.path.basename(input_path))[0]
            output_path = os.path.join(output_dir, f"{base_name}.webp")
            img.save(output_path, "WEBP", quality=90)
            print(f"  ∟ ✅ {output_path}")
    except Exception as e:
        print(f"  ∟ ❌ {input_path} の処理中にエラー: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="画像をWebPに一括変換するツール")
    parser.add_argument("--mode", choices=["resize", "original"], default="resize", help="実行モード: resize (16:9クロップ＆3サイズ生成), original (元サイズのまま変換)")
    parser.add_argument("--input", default="raw_assets", help="入力フォルダのパス (デフォルト: raw_assets)")
    parser.add_argument("--output", default="dist", help="出力フォルダのパス (デフォルト: dist)")
    
    args = parser.parse_args()
    
    process_all_images(input_dir=args.input, output_dir=args.output, mode=args.mode)