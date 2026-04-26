# Image resize tool
画像を指定のサイズにリサイズするPythonスクリプトです。
1枚の元画像から、 $1600 \times 900$ (@2x) と、 $800 \times 450$ (1x) の2サイズを、アスペクト比を16:9に合わせて書き出します。

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

1.  raw_assetsフォルダに元画像を置きます。
2.  スクリプト内の画像パス（例: `sample.jpg`）を書き換えます。
3.  以下のコマンドを実行します。

```bash
python image_gen.py
```

実行後、`dist/` フォルダの中に以下のファイルが生成されます。
* `filename@2x.jpg` ($1600 \times 900$)
* `filename.jpg` ($800 \times 450$)

---