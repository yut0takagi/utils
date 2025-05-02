
# 🛠️ utils

このリポジトリは、PDF 編集を目的とした Python および Jupyter Notebook のユーティリティを含んでいます。

## 📁 ファイル構成

- `edit_pdf.py`：PDF 編集に関連する関数やスクリプトを含む Python ファイル。
- `dev.ipynb`：PDF 編集機能の開発やテストを行うための Jupyter Notebook。
- `requirements.txt`：必要な Python パッケージを記載したファイル。
- `Pipfile` / `Pipfile.lock`：Pipenv を使用した依存関係管理ファイル。

## 🚀 インストール方法

1. このリポジトリをクローンします：

   ```bash
   git clone https://github.com/yut0takagi/utils.git
   cd utils
   ```

2. 必要な Python パッケージをインストールします：

   ```bash
   pip install -r requirements.txt
   ```

   または Pipenv を使用する場合：

   ```bash
   pipenv install
   ```

## 🧪 使用方法

### Python スクリプトを使用する場合

```bash
python edit_pdf.py
```

### Jupyter Notebook を使用する場合

1. Jupyter Notebook を起動します：

   ```bash
   jupyter notebook
   ```

2. ブラウザで `dev.ipynb` を開き、セルを順に実行します。

## 🛠 開発環境

- Python 3.x
- Jupyter Notebook
- 必要なライブラリ（例：`PyPDF2`、`reportlab` など）

## 📄 ライセンス

このプロジェクトのライセンス情報は記載されていません。使用や再配布を行う際は、リポジトリ所有者に確認してください。
