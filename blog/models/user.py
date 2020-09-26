from blog.blog_post import db


class User(db.Model):
    __tablename__  = 'users'

    pk = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(10))
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<User {self.pk} {self.first_name} {self.last_name}>"
