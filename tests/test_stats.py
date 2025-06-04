import pandas as pd

from datamunch import io, stats


def test_summarize() -> None:
    df = io.read_table("tests/fixtures/sample.csv")
    summary = stats.summarize(df)
    assert summary.loc["A", "max"] == 13
