from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix='/off')

from . import routes