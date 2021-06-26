from flask.helpers import get_debug_flag

from macacahub.app import create_app
from macacahub.settings import DevConfig, ProdConfig

CONFIG = DevConfig if get_debug_flag() else ProdConfig

app = create_app(CONFIG)
