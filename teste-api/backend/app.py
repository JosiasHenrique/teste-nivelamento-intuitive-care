from flask import Flask
from flask_cors import CORS
from controller.operadora_controller import buscar_operadora

app = Flask(__name__)

CORS(app)

# Rota para buscar operadora
app.add_url_rule('/buscar', 'buscar_operadora', buscar_operadora, methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True)
