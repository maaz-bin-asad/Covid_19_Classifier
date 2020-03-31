from datetime import datetime
from app1 import db


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     oxygen_concentration = db.Column(db.Integer, nullable=False)
#     dry_cough = db.Column(db.String(20), nullable=False)
#     septic_shock = db.Column(db.String(20), nullable=False)
#     age = db.Column(db.Integer, nullable=False)
#     breathe_rate = db.Column(db.Integer, nullable=False)
#     prior_disease = db.Column(db.String(20), nullable=False)
#
#     def __repr__(self):
#         return f"User('{self.oxygen_concentration}', '{self.dry_cough}', '{self.septic_shock}', '{self.age}', '{self.breathe_rate}', '{self.prior_disease}')"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    string1 = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"{self.string1}"
