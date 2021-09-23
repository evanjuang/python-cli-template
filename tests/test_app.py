from click.testing import CliRunner
from cli_app.cli import cli

runner = CliRunner()


def test_app_foo_baz():
    response = runner.invoke(cli, ["foo", "baz", "-o", "123"])
    assert response.exit_code == 0
