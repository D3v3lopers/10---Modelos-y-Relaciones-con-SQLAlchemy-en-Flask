#10 - Modelos y Relaciones con SQLAlchemy en Flask
from flask import Flask, render_template
from models import db, Producto, Categoria

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/tienda'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    productos = Producto.query.all()
    return render_template('productos.html', productos=productos)

if __name__ == '__main__':
    app.run(debug=True)
