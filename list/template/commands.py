import click

@click.group()
def list():
    pass

@list.command()
def template():
    click.echo("List templates")