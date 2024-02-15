"""Model for Animal Table"""
import uuid
from app.db.config import db

class Animal(db.Model):
    """Animal Class Model"""
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    binomial_name = db.Column(db.String(100), nullable=False)
    genus = db.Column(db.String(100), nullable=False)
    family = db.Column(db.String(100), nullable=False)
    order = db.Column(db.String(100), nullable=False)
    class_column = db.Column(db.String(100), nullable=False, name="class")
    phylum = db.Column(db.String(100), nullable=False)

    def as_dict(self):
        """Animal Dictionary"""
        return {
            "id": self.id,
            "name": self.name,
            "binomial_name": self.binomial_name,
            "genus": self.genus,
            "family": self.family,
            "order": self.order,
            "class": self.class_column,
            "phylum": self.phylum
        }
