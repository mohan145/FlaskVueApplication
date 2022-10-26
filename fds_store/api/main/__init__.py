
from flask import Flask

from flasl_cors import CORS

from config import  Configuration



app = None
cors = CORS(app ,resource= {r"/api/*": { "origins" : ["192.136.5.9"]}})


def create_app(env = None):
    app = Flask(__name__)
    app.config.from_object(Configuration['DEV'])
    app.run(host = '0.0.0.0', port = 5000)

if __name__ == '__main__':
    create_app()
