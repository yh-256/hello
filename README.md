# datamunch

`datamunch` は、CSV / TSV / Excel ファイルから統計情報を手早く算出して表示するための Python 製 CLI ツールです。`pandas` の計算能力を活用し、表形式データの「ざっくり把握」を Markdown テーブルまたは JSON で出力します。

## 主な特徴
- **幅広い入力形式**: `.csv` / `.tsv` / `.xls(x)` を自動判別して読み込み。
- **標準指標の網羅**: count / mean / median / std / min / max を一括計算。
- **柔軟な出力**: Markdown テーブル（デフォルト）と JSON をサポートし、レポート作成や自動処理に活用可能。
- **シンプルな CLI**: `datamunch stats <file> [--format json|md]` だけで利用開始。

## インストール
PyPI からインストールするか、リポジトリをクローンしてローカルインストールしてください。

```bash
pip install datamunch
# または
pip install -e .
```

## 使い方
基本的なコマンドは `stats` のみです。ファイルを指定すると列ごとの統計量が表示されます。

```bash
$ datamunch stats tests/fixtures/sample.csv
```

### 出力形式の切り替え
```bash
$ datamunch stats tests/fixtures/sample.csv --format md   # Markdown (デフォルト)
$ datamunch stats tests/fixtures/sample.csv --format json # JSON
```

## サンプル出力
Markdown テーブル例:

```
|    |   count |   mean |   median |   std |   min |   max |
|:---|--------:|-------:|---------:|------:|------:|------:|
| A  |       5 |      7 |        7 |   4.0 |     1 |    13 |
| B  |       5 |      8 |        8 |   4.0 |     2 |    14 |
| C  |       5 |      9 |        9 |   4.0 |     3 |    15 |
```

JSON 例:

```json
{
  "A": {"count": 5, "mean": 7.0, "median": 7.0, "std": 4.0, "min": 1, "max": 13},
  "B": {"count": 5, "mean": 8.0, "median": 8.0, "std": 4.0, "min": 2, "max": 14}
}
```

## CLI リファレンス
| コマンド | 説明 |
| --- | --- |
| `datamunch stats <file>` | ファイルの統計量を計算。`--format md/json` で出力形式を指定。 |

## 開発者向け
1. 依存関係をインストール: `pip install -r requirements.txt`
2. テストを実行: `pytest`
3. コード整形・静的解析 (任意): `flake8`, `black`, `pre-commit run --all-files`

Pull Request を送る前にテストと lint を通すことを推奨します。
