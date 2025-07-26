import click

import commands


@click.group()
def cli():
    pass


@click.command(name="init")
def init() -> None:
    """Initialises mvog repository."""
    commands._init()


cli.add_command(init)

if __name__ == "__main__":
    cli()
