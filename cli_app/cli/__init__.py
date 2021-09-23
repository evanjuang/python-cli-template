import click
import importlib
import pkgutil
import cli_app


@click.version_option(version=cli_app.__version__, prog_name=cli_app.__title__)
@click.group()
def cli():
    pass


for _, name, _ in pkgutil.walk_packages(__path__, prefix=__name__ + "."):
    try:
        m = importlib.import_module(name)
        c = getattr(m, 'cli')
        cli.add_command(c)

    except Exception:
        pass
