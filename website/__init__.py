from flask import Flask
from config import Config

app = Flask(__name__,
    static_url_path='',
    static_folder="static",
    template_folder='templates'
    )

app.config.from_object(Config)
from website import routing

