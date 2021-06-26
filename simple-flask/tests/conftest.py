import pytest
from webtest import TestApp

from macacahub.app import create_app
from macacahub.settings import TestConfig


@pytest.fixture(scope="function")
def app():
    _app = create_app(TestConfig)

    context = _app.test_request_context()
    context.push()

    yield _app

    context.pop()


@pytest.fixture(scope="function")
def testapp(app):
    """A Webtest app."""
    yield TestApp(app)
