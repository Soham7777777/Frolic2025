import click


@click.command()
def test() -> None:
    """Run tests.
    """        
    import tests
    tests.run()