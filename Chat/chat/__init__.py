from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
import os

app = Flask(__name__)


##################################
#              DB                #
##################################

DB_FILE='site.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///{}'.format(DB_FILE)
app.config['SECRET_KEY'] = 'secret!'


db=SQLAlchemy(app)


from chat.models import Conversation

if os.path.exists("{}".format(DB_FILE)):
    print("it exists, not creating database")

else:# GET DB to preload.
    db.create_all()
chat_room = Conversation()
db.session.add(chat_room)
db.session.commit()

##################################
#           Resources            #
##################################

api = Api(app)


from chat import resources




