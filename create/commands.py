import click
import time
from progress.bar import ChargingBar

@click.group()
def create():
    pass

@click.option('--env', '-e', default='', help='environment')
@click.argument('stack_name')
@create.command()
def stack(env, stack_name):
    if env != "":
        click.echo('Using env {0}'.format(env))
    click.echo('Start stack {0} creation...'.format(stack_name))
    download('Building {0} stack'.format(stack_name), 200)
    click.echo('Stack {0} created successfully!'.format(stack_name))

@create.command()
def template():
    click.echo("Create a template")

def download(message, value):
    bar = ChargingBar(message, max=value)
    for i in range(value):
        time.sleep(0.010)
        bar.next()
    bar.finish()