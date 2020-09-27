from blog.blog_post import db
from blog.models.user import User
from blog.models.contact import Email


def save_user(user_data):
    user = User(first_name=user_data.first_name, last_name=user_data.last_name)
    db.session.add(user)
    db.session.flush()
    return user.pk


def save_email(email_data, user_pk):
    email = Email(email=email_data.email, user=user_pk, is_primary=email_data.is_primary)
    db.session.add(email)
    db.session.flush()