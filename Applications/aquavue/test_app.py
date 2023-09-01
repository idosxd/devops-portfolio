import pytest
from flask import Flask
from database import db, Brand, get_elite_brands, get_non_elite_brands, get_all_brands

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    with app.app_context():
        db.create_all()

    yield app

    with app.app_context():
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_brands_lists(app, client):
    with app.app_context():
        brand1 = Brand(name='Evian', elite=True, imglink="https://m.media-amazon.com/images/I/71uWQtrgz9L.jpg")
        brand2 = Brand(name='Perrier', elite=False, imglink="https://m.media-amazon.com/images/I/71yezRmNcHL.jpg")
        brand3 = Brand(name='San Pellegrino', elite=False, imglink="https://www.sanpellegrino.com/us/sites/g/files/xknfdk2166/files/styles/product_fallback/public/2022-11/sp-img-gallery-product-750-glass.jpg?itok=4EsP91ux")
        brand4 = Brand(name='Spa-Water', elite=False, imglink="https://media.istockphoto.com/id/459234465/photo/spa-water-bottle.jpg?s=612x612&w=0&k=20&c=544xb1BLuoERnUNcbF6giXrmqrzsLBWRQPKmPZpKH8k=")
        brand5 = Brand(name='Volvic', elite=True, imglink="https://m.media-amazon.com/images/I/51lhXkSp2cL.jpg")
        brand6 = Brand(name='Voss', elite=True, imglink="https://produits.bienmanger.com/36932-0w470h470_Voss_Sparkling_Water_From_Norway.jpg")

        db.session.add(brand1)
        db.session.add(brand2)
        db.session.add(brand3)
        db.session.add(brand4)
        db.session.add(brand5)
        db.session.add(brand6)
        db.session.commit()

        all_brands = get_all_brands()
        assert len(all_brands) == 6
        elite_brand = get_elite_brands()
        assert len(elite_brands) == 3
        non_elite_brand = get_non_elite_brands()
        assert len(non_elite_brands) == 3

