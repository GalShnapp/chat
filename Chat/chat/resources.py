from flask_restful import Resource, reqparse
from chat import db, api, chat_room
from chat.models import Conversation, Single_Msg
import json


msg_put_args = reqparse.RequestParser()
msg_put_args.add_argument("sender", type=str, help="your name, luv?", required = True)
msg_put_args.add_argument("payload", type=str, help="Whatcha gotta say", required = True)
MSGS = []


print(chat_room)

class Msg(Resource):
    def get(self):
#        con = Conversation.query.all()
        return json.dumps(MSGS)

    def post(self):
        args = msg_put_args.parse_args()
        MSGS.append(args)
        msg = Single_Msg(sender=args["sender"], payload=args["payload"],conversation=chat_room.id)
        db.session.add(msg)
        db.session.commit()
        return args, 201


api.add_resource(Msg, "/msg")