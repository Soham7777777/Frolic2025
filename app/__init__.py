from flask import Flask
import click
import os


@click.command()
def _test() -> None:
    """Run tests.
    """        
    import tests
    tests.run()


def make_app() -> Flask:
    application = Flask(__name__)

    application.config.from_object(f'instance.{os.getenv('PROFILE', 'Development')}')

    from .blueprints import blog, admin
    application.register_blueprint(blog.bp)
    application.register_blueprint(admin.bp)

    application.cli.add_command(_test, name='test')
    return application