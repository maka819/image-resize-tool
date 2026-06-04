# Image resize tool
画像を指定のサイズにリサイズ、または元のサイズのままWebP形式に変換するPythonスクリプトです。
デフォルトのモードでは、1枚の元画像から、以下サイズの画像をアスペクト比を16:9に合わせてWebP形式で書き出します。
* $2560 \times 1440$
* $1600 \times 900$
* $800 \times 450$

---

## 🛠 準備

### 1. Pythonの確認
Python 3.x がインストールされていることを確認してください。

### 2. 依存ライブラリのインストール

```bash
pip install Pillow
```

---

## 🚀 使い方

1.  デフォルトでは `raw_assets` フォルダに元画像を置きます。
2.  以下のコマンドを実行します。

### 基本的な実行（16:9クロップ＆3サイズへリサイズ）
```bash
python image_gen.py
```

実行後、`dist/` フォルダの中に以下のファイルが生成されます。
* `filenamefull.jpg` (* $2560 \times 1440$)
* `filename@2x.jpg` ($1600 \times 900$)
* `filename.jpg` ($800 \times 450$)

---