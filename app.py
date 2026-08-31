from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from calculadora import calcular_juros_compostos

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    dados = request.get_json()

    principal = dados.get("principal", 0)
    taxa_mensal = dados.get("taxa_mensal", 0)
    meses = dados.get("meses", 0)
    aporte_mensal = dados.get("aporte_mensal", 0)

    resultado = calcular_juros_compostos(
        principal=principal,
        taxa_mensal=taxa_mensal,
        meses=meses,
        aporte_mensal=aporte_mensal
    )

    return jsonify(resultado)

if __name__ == "__main__":
    app.run(debug=True)