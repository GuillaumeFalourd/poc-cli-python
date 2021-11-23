import click
import click_completion

from create import commands as c
from list import commands as l
from describe import commands as d

# click_completion.init()
# option_type = click.Choice('create list describe'.split())

@click.group()
# @click.argument('option', type=option_type)
def main():
    pass

main.add_command(c.create)
main.add_command(l.list)
main.add_command(d.describe)