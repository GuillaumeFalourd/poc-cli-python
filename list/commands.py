import click

from list.stack import commands as s
from list.template import commands as t

@click.group()
def list():
    pass

# @list.command()
# def stack():
#     click.echo("List stacks")

# @list.command()
# def template():
#     click.echo("List templates")

list.add_command(s.stack)
list.add_command(t.template)