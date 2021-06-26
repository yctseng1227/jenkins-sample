from pathlib import Path
import click

PROJECT_ROOT = Path(__file__).resolve().parent.parent
TEST_PATH = str(PROJECT_ROOT / "tests")


@click.command()
def test():
    import pytest

    return_value = pytest.main([TEST_PATH, "--verbose"])
    exit(return_value)
