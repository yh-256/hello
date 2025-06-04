"""Command-line interface for datamunch."""

import click

from . import io, stats


@click.group()
def cli() -> None:
    """datamunch CLI group."""


@cli.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("--format", "fmt", type=click.Choice(["json", "md"]), default="md")
def stats_cmd(file: str, fmt: str) -> None:
    """Show statistics for FILE."""
    df = io.read_table(file)
    summary = stats.summarize(df)
    if fmt == "json":
        click.echo(stats.to_json(summary))
    else:
        click.echo(stats.to_markdown_table(summary))


def main() -> None:
    """Entry point for console script."""
    cli()


if __name__ == "__main__":
    main()
