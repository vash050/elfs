import os
from pathlib import Path

from flask import Flask

DATABASE = 'sqlite:///elfs.db'
DEBUG = True
SECRET_KEY = 'kdsfhciewjcabshj<?kjJbh**kjk,nc'

UPLOAD_FOLDER = os.path.join(Path(__file__).resolve().parent.parent, 'elfs/static/images')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
