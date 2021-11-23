import click

# Example o dynamic options
def my_option_resolver():
    def decorator(f):
        param_decls = (
            "-c",
            "--count",
            "count",
        )
        attrs = dict(
            default=1,
            help='Number of greetings.'
        )
        click.option(*param_decls, **attrs)(f)

        param_decls = (
            "-n",
            "--name",
            "name",
        )
        attrs = dict(
            prompt='Your name',
            help='The person to greet.'
        )
        click.option(*param_decls, **attrs)(f)
        return f

    return decorator


@click.group()
def list():
    pass


@list.command()
@my_option_resolver()
def template(*args, **kwargs):
    click.echo('args: {}'.format(args))
    click.echo('kwargs: {}'.format(kwargs))
    click.echo("List templates")
