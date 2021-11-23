import click
from create import commands as c
from list import commands as l
from describe import commands as d

@click.group()
def main():
    pass

main.add_command(c.create)
main.add_command(l.list)
main.add_command(d.describe)