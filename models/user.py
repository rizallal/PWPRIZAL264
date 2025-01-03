from extensions import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=False)
    email = db.Column(db.String(200), nullable=False, unique=True)    
    password = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(),onupdate=db.func.now())
    
    def data(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
        }

        
    def save(self):
        db.session.add(self)
        db.session.commit()