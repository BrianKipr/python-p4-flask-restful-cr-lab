from app import db

class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, name, image, price):
        self.name = name
        self.image = image
        self.price = price
