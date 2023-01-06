import os
from pathlib import Path

from fastapi.templating import Jinja2Templates


BASE_PATH = Path(__file__).resolve().parent

templates = Jinja2Templates(directory=str(BASE_PATH / 'templates'))

if os.getenv('DOCKERIZED'):
    host_info = '0.0.0.0'
else:
    host_info = '127.0.0.1'

