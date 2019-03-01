from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail


photos = UploadSet('photos',IMAGES)
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
bootstrap = Bootstrap() 
db = SQLAlchemy()

mail = Mail()


def create_app(config_name):
    app = Flask(__name__)
    #........
    mail.init_app(app)
    #............

    # configure UploadSet
    # configure_uploads(app,photos)

     # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')


    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # setting config
    # from .request import configure_request
    # configure_request(app)


    return app

# from flask import Flask
# from .config import DevConfig
# from flask_bootstrap import Bootstrap
# from flask_sqlalchemy import SQLAlchemy

# bootstrap = Bootstrap()
# db = SQLAlchemy()

# #  Initializing application
# app = Flask(__name__,instance_relative_config = True)
# def create_app(config_name):
#     app = Flask(__name__)
# # Setting up configuration
# app.config.from_object(DevConfig)
# app.config.from_pyfile("config.py")

# # Initializing Flask Extensions
# bootstrap = Bootstrap(app)
# bootstrap.init_app(app)
# db.init_app(app)


from .main import views
from .main import error