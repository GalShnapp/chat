from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)

##################################
#              DB                #
##################################

POSTGRES_USER="postgres"
POSTGRES_PASSWORD="password"
POSTGRES_DB="postgres"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:password@0.0.0.0/postgres'.format(POSTGRES_USER, POSTGRES_PASSWORD,POSTGRES_DB)
# app.config['SECRET_KEY'] = '5791628bb0t13ce0c676dfde280ba245'
print('postgresql set')

db=SQLAlchemy(app)

##################################
#           Resources            #
##################################

api = Api(app)

from chat import resources




