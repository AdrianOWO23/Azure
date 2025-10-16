# Importar la clase Flask
from flask import Flask, render_template
from datetime import datetime

# Crear una instancia de la aplicación Flask
# En AWS Elastic Beanstalk, la variable debe llamarse 'application' por defecto.
# En Azure y GCP, 'app' es el estándar común. Podemos usar el mismo archivo.
application = app = Flask(__name__)

# Definir la ruta raíz ('/') de la aplicación
@app.route('/')
def index():
    products = [
        {'id': 1, 'name': 'Minimal Lamp', 'price': '29.99', 'desc': 'Sleek desktop lamp'},
        {'id': 2, 'name': 'Aurora Speaker', 'price': '59.99', 'desc': 'Compact bluetooth speaker'},
        {'id': 3, 'name': 'Neo Desk Mat', 'price': '14.99', 'desc': 'Soft anti-slip desk mat'},
        {'id': 4, 'name': 'Zen Notebook', 'price': '9.99', 'desc': 'Minimal dotted notebook'}
    ]
    return render_template('index.html', products=products, year=datetime.now().year)

@app.route('/about')
def about():
    return render_template('base.html', title='About', year=datetime.now().year)

# Punto de entrada para ejecutar la aplicación (opcional, bueno para pruebas locales)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)