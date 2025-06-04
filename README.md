# datamunch

A CLI tool to compute statistics from CSV, TSV, or Excel files.

## Installation
```bash
pip install datamunch
```

## Usage
```bash
$ datamunch stats tests/fixtures/sample.csv
```

## Example Output
```bash
$ datamunch stats tests/fixtures/sample.csv
```
```
|    |   count |   mean |   median |   std |   min |   max |
|:---|--------:|-------:|---------:|------:|------:|------:|
| A  |       5 |      7 |        7 |   4.0 |     1 |    13 |
| B  |       5 |      8 |        8 |   4.0 |     2 |    14 |
| C  |       5 |      9 |        9 |   4.0 |     3 |    15 |
```
