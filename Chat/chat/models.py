from chat import db

# Some Buffers - optimize later.
MAX_PAYLOAD_BUFF=1200
MAX_USERNAME_BUFF=25
MAX_PW_BUFF=60


# For fast pull 
class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    msgs = db.relationship('Single_Msg', backref='Conversation') # should I lazy = true? intuition says NO! but, we'll see.
    

class Single_Msg(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(MAX_USERNAME_BUFF), nullable=False)
    payload = db.Column(db.Text, nullable=False)
    conversation =db.Column(db.Integer, db.ForeignKey('conversation.id'), nullable=False)
    

    def __repr__(self):
        return "{}: {}\n".format(self.sender, self.payload)
