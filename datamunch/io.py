"""IO utilities for datamunch."""

from pathlib import Path
from typing import Any

import pandas as pd


def read_table(path: str | Path, **kwargs: Any) -> pd.DataFrame:
    """Read CSV, TSV, or Excel file into a DataFrame.

    Args:
        path: Path to the input file.
        **kwargs: Additional keyword arguments passed to pandas read function.

    Returns:
        DataFrame with file contents.
    """
    p = Path(path)
    if p.suffix.lower() in {".xls", ".xlsx"}:
        return pd.read_excel(p, **kwargs)
    if p.suffix.lower() == ".tsv":
        return pd.read_csv(p, sep="\t", **kwargs)
    return pd.read_csv(p, **kwargs)
