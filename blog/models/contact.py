from blog.blog_post import db
from blog.utils.enums import ContactType


class Email(db.Model):
    __tablename__  = "emails"

    pk = db.Column(db.Integer, primary_key=True)
    type = db.Column(
        db.Enum(ContactType),
        default=ContactType.personal,
        nullable=False
    )
    email = db.Column(db.String, nullable=False, unique=True)
    is_primary = db.Column(db.Boolean, nullable=False)
    user = db.Column(db.Integer, db.ForeignKey('users.pk'), nullable=False)

    def __repr__(self):
        return f'<Email {self.pk} {self.email}>'


class Phone(db.Model):
    __tablename__  = "phones"

    pk = db.Column(db.Integer, primary_key=True)
    type = db.Column(
        db.Enum(ContactType),
        default=ContactType.personal,
        nullable=False
    )
    country_code = db.Column(db.String(7), nullable=False)
    number = db.Column(db.String(20), nullable=False)
    extension = db.Column(db.String(7))
    is_primary = db.Column(db.Boolean, nullable=False)
    user = db.Column(db.Integer, db.ForeignKey('users.pk'), nullable=False)

    def __repr__(self):
        return f'<Phone {self.pk} {self.country_code} ' \
               f'{self.number} {self.extension}>'
