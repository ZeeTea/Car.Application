from app import db

class User(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password_hash = db.Column(db.String(120), nullable=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return f'user: {self.username}'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()