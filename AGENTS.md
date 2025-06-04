# AGENTS.md

## 📌 プロジェクト概要
このリポジトリは、Python製のコマンドラインツール（CLI）を開発するためのものです。実用性と保守性を重視し、モジュール分割・型ヒント・テスト駆動開発（TDD）を推奨します。

## 🔧 使用技術・ツール
- Python 3.11
- 標準ライブラリ重視（`argparse`, `os`, `pathlib`, `logging` など）
- テスト: `pytest`
- 静的解析: `mypy`, `flake8`
- GitHub Actions によるCI/CD

## 🧠 Codexへの指針
- ファイル構成は `src/`, `tests/`, `docs/` に分けてください。
- コメントには docstring（Google style）を使用してください。
- テストはTDDの原則に従ってまず失敗するテストを書くところから始めてください。
- コマンドライン引数の解析は `argparse` で実装してください。
- `README.md` を自動生成してください。

## 🧪 初期タスクの提案
- `README.md` の自動生成（プロジェクトの概要、インストール手順、使い方）
- `main.py` によるエントリーポイント作成（引数処理を含む）
- 初期単体テストの作成（`tests/test_main.py`）
