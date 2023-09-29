from flask import Flask
from config import Config
#from .routes.chat_bp import chat_bp
from .routes.user_route import bp_users
from .routes.server_route import bp_servers
from .routes.canales_route import bp_canales
from APP.database import DatabaseConnection
from flask_cors import CORS, cross_origin
def inicializar_app():
   """Crea y configura la aplicación Flask"""
   app = Flask(__name__, static_folder=Config.STATIC_FOLDER,template_folder=Config.TEMPLATE_FOLDER)
   app.config['CORS_HEADERS'] = 'Content-Type'
   app.config['CORS_SUPPORTS_CREDENTIALS'] = True
   app.config['CORS_SEND_WILDCARD'] = False
   CORS(app, origins='http://127.0.0.1:5501')
   #CORS(app, supports_credentials=True)
   
   app.config.from_object(Config)
   DatabaseConnection.set_config(app.config)
   #app.register_blueprint(chat_bp)
   #app.register_blueprint(actor_bp)
   
   app.register_blueprint(bp_users, url_prefix="/users")
   app.register_blueprint(bp_servers, url_prefix="/server")
   app.register_blueprint(bp_canales, url_prefix="/canales")
   #app .register_blueprint(bp_servers, url_prefix="/messages")
   #app.register_blueprint(errors)
   return app