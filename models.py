from app import db


class Sensor(db.Model):
    """Simple database model to track weather."""

    __tablename__ = 'sensor'
    id = db.Column(db.Integer, primary_key=True)
    s = db.Column(db.String)
    t = db.Column(db.Integer)
    h = db.Column(db.Integer)

    def __init__(self, s, t, h):
        self.s = s
        self.t = t
        self.h = h
