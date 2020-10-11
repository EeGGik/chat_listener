from flask import Flask
from loguru import logger
from urls import add_routes
import os
import sys


app = Flask(__name__)
logger.add(sys.stdout, format="{time} {level} {message}", level=os.environ.get("LOG_LVL", default="INFO"))
app = add_routes(app)
