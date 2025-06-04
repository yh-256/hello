from click.testing import CliRunner

from datamunch.cli import cli


def test_cli_md(tmp_path) -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["stats", "tests/fixtures/sample.csv"])
    assert result.exit_code == 0
    assert "|" in result.output
