from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)

##################################
#              DB                #
##################################

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///site.db'

db=SQLAlchemy(app)


from chat.models import Conversation
db.create_all()
chat_room = Conversation()
db.session.add(chat_room)
db.session.commit()

##################################
#           Resources            #
##################################

api = Api(app)


from chat import resources




