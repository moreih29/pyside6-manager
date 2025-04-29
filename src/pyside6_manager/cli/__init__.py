import click

from .generate_qmltypes import generate_qmltypes
from .. import __version__, __name__


@click.group()
@click.version_option(version=__version__, package_name=__name__, prog_name=__name__)
def cli():
    pass


cli.add_command(generate_qmltypes, name="genqml")
