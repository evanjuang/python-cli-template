import click
from cli_app.api import foo


@click.group(name='foo', help='Command set foo')
def cli():
    pass


@cli.command('file', help='File command')
@click.option('-f', '--my-file', type=click.Path(exists=True), help='Input file')
def __file(my_file):
    foo.foo_file(my_file)


@cli.command('baz', help='Dummy command')
@click.option('-o', '--option', required=True)
def baz(option):
    click.echo(f'baz option={option}')
