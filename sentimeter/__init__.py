import logging
from flask import Flask
from os import environ


app = Flask(__name__)
app.config['DEBUG'] = True
DATABASE_PATH = 'app/Assets/SQLite.db'

# Logger
logger = logging.getLogger('sentimeter')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(
    '%(filename)s: '
    '%(levelname)s: '
    '%(funcName)s(): '
    '%(lineno)d:\t'
    '%(message)s')
)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
import sentimeter.views