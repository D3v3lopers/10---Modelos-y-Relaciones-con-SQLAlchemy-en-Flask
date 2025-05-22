#11. Flask 3.0  Flask y SQLAlchemy CRUD Listar Registros
from flask import Flask, render_template
from models import db, Producto
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/tienda'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    productos = Producto.query.all()
    return render_template('index.html', productos=productos)



if __name__ == '__main__':
    app.run(debug=True)

















