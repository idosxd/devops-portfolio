from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    elite = db.Column(db.Boolean, default=False)
    imglink = db.Column(db.String(500))

def get_all_brands():
    return Brand.query.all()

def get_elite_brands():
    return Brand.query.filter_by(elite=True).all()

def get_non_elite_brands():
    return Brand.query.filter_by(elite=False).all()
