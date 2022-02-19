import os
from flask import Flask, jsonify, request, render_template
from math import sqrt

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('calc.html')


@app.route('/calculaform', methods=['POST', 'GET'])
def calculaform():
    valor1 = request.form['v1']
    valor2 = request.form['v2']
    operacao = request.form['operacao']
    
    print(operacao)
    
    if operacao == 'soma':
        resultado = int(valor1) + int(valor2)
    elif operacao == 'subtracao':
        resultado = int(valor1) - int(valor2)
    elif operacao == 'divisao':
        resultado = int(valor1) / int(valor2)
    elif operacao == 'multiplicacao':
        resultado = int(valor1) * int(valor2)

    return str(resultado)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port)
    