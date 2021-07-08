import json
from json.encoder import JSONEncoder
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


##################################
#              DB                #
##################################

MSGS = []


##################################
#           Resources            #
##################################

class Msg(Resource):
    def get(self):
        MSGS.append({})
        return json.dumps(MSGS)

    def post(self):
        return {}


api.add_resource(Msg, "/msg")

if __name__ == "__main__":
    app.run(debug=True) # TODO: nope.
