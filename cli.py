import click

from apply import commands as a
from create import commands as c
from describe import commands as d
from list import commands as l

@click.group()
def cli():
    pass

@cli.resultcallback()
def process_result(result, **kwargs):
    click.echo('After command')

cli.add_command(a.apply)
cli.add_command(c.create)
cli.add_command(d.describe)
cli.add_command(l.list)

def main():
    cli(prog_name="os")

if __name__ == '__main__':
    main()
