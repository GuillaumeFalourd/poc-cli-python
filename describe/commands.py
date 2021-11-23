import click
import inquirer

DESCRIPTION = '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'''

@click.group()
def describe():
    pass

@describe.command()
def stack():
    questions = [
        inquirer.List('stack',
                        message="What stack do you want to describe?",
                        choices=['Stack 1', 'Stack 2', 'Stack 3', 'Stack 4', 'Stack 5'],
                    ),
        ]
    answers = inquirer.prompt(questions)
    click.echo('{0} description:\n'.format(answers['stack']))
    click.echo(DESCRIPTION)

@describe.command()
def template():
    questions = [
        inquirer.List('template',
                        message="What template do you want to describe?",
                        choices=['Template 1', 'Template 2', 'Template 3', 'Template 4', 'Template 5'],
                    ),
        ]
    answers = inquirer.prompt(questions)
    click.echo('{0} description:\n'.format(answers['template']))
    click.echo(DESCRIPTION)