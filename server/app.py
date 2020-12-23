from flask import Flask, g, request
from flask_restplus import Api
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import flask_jwt_extended as JWT
from .games_api import games_api
from .auth_api import auth_api

from .util import get_config


# Create the app and configure it
app = Flask(__name__)                       # Create Flask app
app.config.update(get_config(app.config['ENV'],
                             app.open_resource('config.yaml')))
CORS(app)
#     headers=['Content-Type', 'Authorization'],
#     expose_headers='Authorization')                                   # Cross-origin resource sharing
api = Api(app, doc=False)                              # Create RESTplus api on app
api.add_namespace(games_api, path='/api/games') # Insert games Namespace
api.add_namespace(auth_api, path='/api/auth')

assert('JWT_SECRET_KEY' in app.config), 'Must set FLASK_JWT_SECRET_KEY env variable'
if 'JWT_ACCESS_TOKEN_EXPIRES' not  in app.config:
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 86400 # default is 1 day

#app.config['JWT_TOKEN_LOCATION'] = ['headers', 'query_string']
app.config['PROPAGATE_EXCEPTIONS'] = True # Avoid server error w/bad JWTs in gunicorn
jwt = JWT.JWTManager(app)  # do thsi after configi set

print('URL MAP', app.url_map)   # useful for debugging

@app.before_request
def init_db():
    '''Initialize db by creating the global db_session

    This runs on each request
    '''
    #print("Method " + request.method + "EndPoint " + request.endpoint + "\n" )
    #print("Request   " + str(dict(request.headers)) + "\n")
    db_auth = create_engine(app.config['DB_AUTH'])
    g.auth_db = sessionmaker(db_auth)()

    db_usage = create_engine(app.config['DB_USAGE'])
    g.usage_db = sessionmaker(db_usage)()

    db_games = create_engine(app.config['DB_GAMES'])
    g.games_db = sessionmaker(db_games)()


@app.teardown_request
def close_db(exception):
    '''Close down db connection, same one cannot be used b/w threads

    This runs on each request
    '''
    if hasattr(g, 'auth_db'):
        g.auth_db.close()
        _ = g.pop('auth_db')

    if hasattr(g, 'usage_db'):
        g.usage_db.close()
        _ = g.pop('usage_db')

    if hasattr(g, 'games_db'):
        g.games_db.close()
        _ = g.pop('games_db')

