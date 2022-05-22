"""Database models"""
from flask_login import UserMixin
from Shopify_imgRepo import db, login_manager


class User(UserMixin, db.Model):
    """table listing users and their log in information """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    passphrase = db.Column(db.String(), nullable=False)
    images = db.relationship('Image', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.first_name

    def get_user_id(self):
        """ Returns user's id"""
        return self.id

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Image(db.Model):
    """table listing all image file names and locations"""
    __tablename__ = "images"

    image_id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String, nullable=False)
    file_location = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.user_id