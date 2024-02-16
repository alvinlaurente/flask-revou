"""Model for Employees Table"""
import uuid
from app.db.config import db

class Employee(db.Model):
    """Employee Class Model"""
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(10), nullable=True)
    schedule = db.Column(db.String(100), nullable=True)

    def as_dict(self):
        """Employee Dictionary"""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "role": self.role,
            "schedule": self.schedule
        }
