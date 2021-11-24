import click

from apply.plugin import functions as p

@click.group()
def apply():
    pass

@click.option('--language', '-l', default='', help='language')
@click.argument('stack_name')
@apply.command()
def plugin(language, stack_name):
    if language != "":
        click.echo('Using language {0}'.format(language))
    p.plugin(language, stack_name)