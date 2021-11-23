import click

from create import commands as c
from list import commands as l
from describe import commands as d

@click.group()
def cli():
    pass


cli.add_command(c.create)
cli.add_command(l.list)
cli.add_command(d.describe)

def main():
    cli(prog_name="os")

if __name__ == '__main__':
    main()
