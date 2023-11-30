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
    
class users(db.Model):
    userId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(300), unique=False)
    avatarImage = db.Column(db.String(500), unique=False)  # new field

    def to_dict(self):
        return {
            'userId': self.userId,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'avatarImage': self.avatarImage,  # include new field in dict
        }
class orders(db.Model):
    orderId = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.userId'), nullable=False)
    productId = db.Column(db.Integer, db.ForeignKey('products.productId'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Float, nullable=False)

    def __init__(self, userId, productId, quantity, total):
        self.userId = userId
        self.productId = productId
        self.quantity = quantity
        self.total = total

    def to_dict(self):
        return {
            'orderId': self.orderId,
            'userId': self.userId,
            'productId': self.productId,
            'quantity': self.quantity,
            'total': self.total
        }