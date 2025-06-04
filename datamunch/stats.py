"""Statistics utilities for datamunch."""

from __future__ import annotations

from typing import Any, Dict

import pandas as pd


def summarize(df: pd.DataFrame) -> pd.DataFrame:
    """Compute statistics for numeric columns.

    Args:
        df: DataFrame to summarize.

    Returns:
        DataFrame with statistics (count, mean, median, std, min, max).
    """
    numeric_df = df.select_dtypes(include="number")
    return pd.DataFrame({
        "count": numeric_df.count(),
        "mean": numeric_df.mean(),
        "median": numeric_df.median(),
        "std": numeric_df.std(),
        "min": numeric_df.min(),
        "max": numeric_df.max(),
    })


def to_markdown_table(stats_df: pd.DataFrame) -> str:
    """Convert DataFrame to Markdown table."""
    return stats_df.to_markdown()


def to_json(stats_df: pd.DataFrame) -> str:
    """Convert DataFrame to JSON string."""
    return stats_df.to_json(orient="index")
