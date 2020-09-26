from blog.blog_post import db


class Post(db.Model):
    __tablename__ = "posts"

    pk = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(160), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user = db.Column(db.Integer, db.ForeignKey('users.pk'), nullable=False)

    def __repr__(self):
        return f"<Post {self.pk} {self.Title}>"
