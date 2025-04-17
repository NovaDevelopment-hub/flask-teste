# app.py
from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('form.html')

@app.route('/admin')
def admin():
    with open('dados.json', 'r') as f:
        dados = json.load(f)
    return render_template('admin.html', cadastros=dados)

@app.route('/enviar', methods=['POST'])
def enviar():
    novo_dado = request.json
    try:
        with open('dados.json', 'r') as f:
            dados = json.load(f)
    except FileNotFoundError:
        dados = []

    dados.append(novo_dado)

    with open('dados.json', 'w') as f:
        json.dump(dados, f, indent=2)

    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True)
