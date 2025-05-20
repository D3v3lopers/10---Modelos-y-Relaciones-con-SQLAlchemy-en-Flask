from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Producto(db.Model):
    __tablename__ = 'producto'

    id_producto = db.Column(db.Integer, primary_key=True)
    nombre_producto = db.Column(db.String(100), nullable=True)
    precio_producto = db.Column(db.Float, nullable=True)

    categoria_id_categoria = db.Column(db.Integer, db.ForeignKey('categoria.id_categoria'), nullable=False)

    def __repr__(self):
        return f"<Producto {self.nombre_producto} - Precio: {self.precio_producto}>"


class Categoria(db.Model):
    __tablename__ = 'categoria'

    id_categoria = db.Column(db.Integer, primary_key=True)
    nombre_categoria = db.Column(db.String(100), nullable=True)

    productos = db.relationship('Producto', backref='categoria', lazy=True)

    def __repr__(self):
        return f"<Categoria {self.nombre_categoria}>"