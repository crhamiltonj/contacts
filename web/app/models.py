from .db import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return f'<Contact {first_name} {last_name}>'

    def save_to_db(self):
        pass