import typer

from .generate_qmltypes import router
from .. import __version__, __name__

app = typer.Typer()
app.add_typer(router)


def version_callback(value: bool):
    if value:
        typer.echo(f"{__name__} {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(False, "--version", "-v", callback=version_callback),
):
    """
    PySide6 Manager CLI tool
    """
    pass
