from flask import Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import sys
sys.path.append(".")

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/api_pobreza'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



from ESECAF.controllers.ApiController import  ApiRoute
app.register_blueprint(ApiRoute, url_prefix='/api')

from ESECAF.controllers.ProyectController import  ProyectRoute
app.register_blueprint(ProyectRoute, url_prefix='/')