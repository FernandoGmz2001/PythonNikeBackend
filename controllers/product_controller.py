from flask import Blueprint, request, send_file
import pandas as pd
from openpyxl import Workbook
from controllers.models_folder.models import db, products
from openpyxl.utils.dataframe import dataframe_to_rows

product_routes = Blueprint('product_routes', __name__)

@product_routes.route('/products', methods=['GET'])
def get_all_products():
    productos = products.query.all()
    return {'productos': [producto.to_dict() for producto in productos]}, 200

@product_routes.route('/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    product = products.query.get(product_id)
    if product:
        return {
            'productId': product.productId,
            'productName': product.productName,
            'productImage': product.productImage,
            'productPrice': product.productPrice,
            'productDescription': product.productDescription,
            'productGender': product.productGender
        }, 200
    else:
        return {'error': 'Producto no encontrado'}, 404

@product_routes.route('/products', methods=['POST'])
def create_products():
    product_data = request.get_json()  
    if isinstance(product_data, list):  # Verifica si los datos son una lista
        for data in product_data:
            # Verifica si el producto ya existe en la base de datos
            existing_product = products.query.filter_by(productName=data['productName']).first()
            if existing_product is None:
                nuevo_producto = products(
                    productName=data['productName'],
                    productImage=data['productImage'],
                    productPrice=data['productPrice'],
                    productDescription=data['productDescription'],
                    productGender=data['productGender']
                )
                db.session.add(nuevo_producto)
        db.session.commit()
        return {'message': 'Productos creados exitosamente'}, 201
    elif isinstance(product_data, dict):  # Verifica si los datos son un diccionario
        # Verifica si el producto ya existe en la base de datos
        existing_product = products.query.filter_by(productName=product_data['productName']).first()
        if existing_product is None:
            nuevo_producto = products(
                productName=product_data['productName'],
                productImage=product_data['productImage'],
                productPrice=product_data['productPrice'],
                productDescription=product_data['productDescription'],
                productGender=product_data['productGender']
            )
            db.session.add(nuevo_producto)
            db.session.commit()
            return {'message': 'Producto creado exitosamente'}, 201
        else:
            return {'message': 'El producto ya existe'}, 200
    else:
        return {'error': 'Los datos enviados no son válidos'}, 400

@product_routes.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id, product_data):
    product = products.query.get(product_id)
    if product:
        product.productName = product_data['productName']
        product.productImage = product_data['productImage']
        product.productPrice = product_data['productPrice']
        product.productDescription = product_data['productDescription']
        product.productGender = product_data['productGender']
        db.session.commit()
        return {'message': 'Producto actualizado exitosamente'}, 200
    else:
        return {'error': 'Producto no encontrado'}, 404

@product_routes.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    producto = products.query.get(product_id)
    if producto:
        db.session.delete(producto)
        db.session.commit()
        return {'message': 'Producto eliminado exitosamente'}, 200
    else:
        return {'error': 'Producto no encontrado'}, 404

@product_routes.route('/products/<string:product_name>', methods=['DELETE'])
def delete_product_by_name(product_name):
    producto = products.query.filter_by(productName=product_name).first()
    if producto:
        db.session.delete(producto)
        db.session.commit()
        return {'message': 'Producto eliminado exitosamente'}, 200
    else:
        return {'error': 'Producto no encontrado'}, 404

@product_routes.route('/products/export', methods=['GET'])
def export_products():
    # Obtener todos los productos de la base de datos
    all_products = products.query.all()

    # Crear un DataFrame de pandas con los datos de los productos
    data = {
        'Product ID': [product.productId for product in all_products],
        'Product Name': [product.productName for product in all_products],
        'Product Image': [product.productImage for product in all_products],
        'Product Price': [product.productPrice for product in all_products],
        'Product Description': [product.productDescription for product in all_products],
        'Product Gender': [product.productGender for product in all_products]
    }
    df = pd.DataFrame(data)

    # Crear un nuevo archivo de Excel y guardar los datos del DataFrame en él
    workbook = Workbook()
    sheet = workbook.active
    for row in dataframe_to_rows(df, index=False, header=True):
        sheet.append(row)

    # Guardar el archivo de Excel
    filename = 'products.xlsx'
    workbook.save(filename)

    return send_file(filename, as_attachment=True)