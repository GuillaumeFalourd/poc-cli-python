import click

@click.group()
def list():
    pass

@list.command()
def stack():
    click.echo("List stacks")
