import typer

from pyside6_manager.cli.generate_qmltypes import (
    generate_qmltypes as generate_qmltypes_command,
)

app = typer.Typer()


@app.command()
def generate_qmltypes(
    file_path: str = typer.Option(..., "--file", "-f"),
    output_file: str = typer.Option(..., "--output", "-o"),
):
    print(file_path)
    generate_qmltypes_command(file_path, output_file)


if __name__ == "__main__":
    app()
