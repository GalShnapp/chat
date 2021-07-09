import json
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


##################################
#              DB                #
##################################

msg_put_args = reqparse.RequestParser()
msg_put_args.add_argument("sender", type=str, help="your name, luv?", required = True)
msg_put_args.add_argument("payload", type=str, help="Whatcha gotta say", required = True)
MSGS = []


##################################
#           Resources            #
##################################

class Msg(Resource):
    def get(self):
        return json.dumps(MSGS)

    def put(self):
        args = msg_put_args.parse_args()
        MSGS.append(args)
        return {}, 201


api.add_resource(Msg, "/msg")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True) # TODO: these should all be taken from some conf file. 
                                                   #       probably share it with docker..
