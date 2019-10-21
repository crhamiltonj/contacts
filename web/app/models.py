from .db import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return f'<Contact {first_name} {last_name}>'

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_last_name(cls, last_name):
        found_contacts = Contact.query.filter_by(last_name=last_name).all()
        return found_contacts