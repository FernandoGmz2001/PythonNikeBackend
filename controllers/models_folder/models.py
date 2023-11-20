from app import db

class products(db.Model):
    productId = db.Column(db.Integer, primary_key=True,autoincrement=True)
    productName = db.Column(db.String(100), unique=True)
    productImage = db.Column(db.String(400), unique=False)
    productPrice = db.Column(db.Integer, unique=False)
    productDescription = db.Column(db.String(500), unique=False)
    productGender = db.Column(db.String(200), unique=False)

    def to_dict(self):
        return {
            'productId': self.productId,
            'productName': self.productName,
            'productImage': self.productImage,
            'productPrice': self.productPrice,
            'productDescription': self.productDescription,
            'productGender': self.productGender
        }